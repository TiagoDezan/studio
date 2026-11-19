import type { APIRoute } from 'astro';
import { isAdmin } from '../../lib/auth';
import { updateSettings, updateLead, deleteLead, resetStats, getSettings } from '../../lib/store';
import { projects } from '../../data/content';

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
      const ids = projects.map((p) => p.id);
      const hidden = ids.filter((id) => fd.get('show:' + id) !== 'on');
      const order = [...ids].sort((a, b) => Number(fd.get('order:' + a) || 99) - Number(fd.get('order:' + b) || 99));
      updateSettings({ hiddenProjects: hidden, projectOrder: order });
      return back('projetos');
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
