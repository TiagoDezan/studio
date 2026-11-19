import type { APIRoute } from 'astro';
import { isAdmin } from '../../lib/auth';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { randomUUID } from 'node:crypto';
import { updateSettings, updateLead, deleteLead, resetStats, getSettings, getProjects, saveProject, deleteProject, setProjectsVisibility, UPLOAD_DIR, type StoredProject } from '../../lib/store';

const IMG_TYPES: Record<string, string> = { 'image/png': 'png', 'image/jpeg': 'jpg', 'image/webp': 'webp', 'image/svg+xml': 'svg', 'image/avif': 'avif', 'image/gif': 'gif' };
const slug = (v: string) => v.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 40) || 'projeto';
const tri = (fd: FormData, k: string, n = 600) => ({ pt: str(fd, k + '_pt', n), es: str(fd, k + '_es', n), en: str(fd, k + '_en', n) });

async function removeUpload(image?: string) {
  if (image?.startsWith('/media/')) await fs.rm(path.join(UPLOAD_DIR, path.basename(image)), { force: true }).catch(() => {});
}

const str = (fd: FormData, k: string, n = 300) => String(fd.get(k) ?? '').trim().slice(0, n);

export const POST: APIRoute = async ({ request, cookies, redirect }) => {
  if (!isAdmin(cookies)) return redirect('/painel', 303);
  const fd = await request.formData();
  const action = str(fd, 'action', 40);
  const back = (tab: string, ok = 'saved') => redirect(`/painel?tab=${tab}&ok=${ok}`, 303);

  switch (action) {
    case 'settings': {
      const webhook = str(fd, 'webhookUrl', 500);
      updateSettings({
        available: fd.get('available') === 'on',
        maintenance: fd.get('maintenance') === 'on',
        announcement: { enabled: fd.get('announcementEnabled') === 'on', text: str(fd, 'announcementText', 200) },
        email: str(fd, 'email', 160),
        whatsapp: str(fd, 'whatsapp', 40),
        instagram: str(fd, 'instagram', 60),
        webhookUrl: /^https:\/\//.test(webhook) ? webhook : '',
      });
      return back('site');
    }
    case 'projects': {
      const map: Record<string, { visible: boolean; order: number }> = {};
      for (const p of getProjects()) map[p.id] = { visible: fd.get('show:' + p.id) === 'on', order: Number(fd.get('order:' + p.id) || 99) };
      setProjectsVisibility(map);
      return back('projetos');
    }
    case 'projectSave': {
      const existing = getProjects().find((p) => p.id === str(fd, 'id', 60));
      const name = str(fd, 'name', 120);
      if (!name) return redirect(`/painel?tab=projetos&edit=${existing?.id ?? 'new'}&ok=missing`, 303);
      let id = existing?.id;
      if (!id) {
        id = slug(name);
        while (getProjects().some((p) => p.id === id)) id = slug(name) + '-' + randomUUID().slice(0, 4);
      }
      let image = existing?.image ?? '';
      const file = fd.get('imageFile');
      if (file instanceof File && file.size > 0) {
        const ext = IMG_TYPES[file.type];
        if (!ext || file.size > 8 * 1024 * 1024) return redirect(`/painel?tab=projetos&edit=${existing?.id ?? 'new'}&ok=badimg`, 303);
        await fs.mkdir(UPLOAD_DIR, { recursive: true });
        const fname = `${id}-${Date.now().toString(36)}.${ext}`;
        await fs.writeFile(path.join(UPLOAD_DIR, fname), Buffer.from(await file.arrayBuffer()));
        await removeUpload(existing?.image);
        image = '/media/' + fname;
      } else if (fd.get('removeImage') === 'on') {
        await removeUpload(existing?.image);
        image = '';
      }
      const url = str(fd, 'url', 300);
      const bg = str(fd, 'imageBg', 20);
      const p: StoredProject = {
        id,
        kind: fd.get('kind') === 'client' ? 'client' : 'own',
        name,
        tag: tri(fd, 'tag', 80),
        summary: tri(fd, 'summary', 700),
        stack: str(fd, 'stack', 300).split(',').map((x) => x.trim()).filter(Boolean).slice(0, 12),
        image,
        imageFit: fd.get('imageFit') === 'contain' ? 'contain' : 'cover',
        imageBg: /^#[0-9a-fA-F]{3,8}$/.test(bg) ? bg : undefined,
        url: /^https?:\/\//.test(url) ? url : undefined,
        urlLabel: tri(fd, 'urlLabel', 60),
        status: tri(fd, 'status', 40),
        visible: fd.get('visible') === 'on',
        order: Number(fd.get('order') || existing?.order || getProjects().length + 1),
      };
      saveProject(p);
      return back('projetos');
    }
    case 'projectDelete': {
      const p = deleteProject(str(fd, 'id', 60));
      await removeUpload(p?.image);
      return back('projetos', 'pdeleted');
    }
    case 'toggleMaintenance':
      updateSettings({ maintenance: !getSettings().maintenance });
      return back('geral');
    case 'leadRead':
      updateLead(str(fd, 'id', 60), { read: fd.get('value') === '1' });
      return back('mensagens', 'lead');
    case 'leadStar':
      updateLead(str(fd, 'id', 60), { starred: fd.get('value') === '1' });
      return back('mensagens', 'lead');
    case 'leadDelete':
      deleteLead(str(fd, 'id', 60));
      return back('mensagens', 'deleted');
    case 'resetStats':
      resetStats();
      return back('dados', 'reset');
  }
  return back('geral', 'noop');
};
