import sys,glob,os,cv2,numpy as np,qrcode
from PIL import Image,ImageDraw,ImageFont
SRC,DST=sys.argv[1],sys.argv[2]
FONT='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
FAKE='VN-26-014-C'
def qrimg(n):
    q=qrcode.QRCode(border=0,error_correction=qrcode.constants.ERROR_CORRECT_M);q.add_data('https://my.reunio.app');q.make()
    return q.make_image(fill_color='#0b1a1d',back_color='white').convert('RGB').resize((n,n),Image.NEAREST)
for f in sorted(glob.glob(SRC+'/**/*.png',recursive=True)):
    im=Image.open(f).convert('RGB');a=np.array(im).astype(int)
    m=((abs(a[:,:,0]-140)<=4)&(abs(a[:,:,1]-150)<=4)&(abs(a[:,:,2]-150)<=4)).astype(np.uint8)
    n,lab,st,_=cv2.connectedComponentsWithStats(m,8)
    d=ImageDraw.Draw(im);changed=0
    for i in range(1,n):
        x,y,w,h,ar=st[i]
        if ar<3000 or ar<0.8*w*h: continue
        changed+=1
        if w>50 and h>50 and 0.6<w/h<1.6:
            d.rounded_rectangle((x,y,x+w,y+h),radius=int(min(w,h)*.06),fill='white')
            s=int(min(w,h)*.88);q=qrimg(s);im.paste(q,(x+(w-s)//2,y+(h-s)//2))
        else:
            bg=tuple(int(v) for v in a[y+h//2,max(0,x-6)])
            dark=sum(bg)<360
            d.rounded_rectangle((x-2,y-2,x+w+2,y+h+2),radius=8,fill=bg)
            fs=int(h*.62);fnt=ImageFont.truetype(FONT,fs)
            d.text((x if dark else x+w//2,y+h//2),FAKE,font=fnt,fill=(234,240,238) if dark else (40,48,50),anchor='lm' if dark else 'mm')
    out=os.path.join(DST,os.path.relpath(f,SRC));os.makedirs(os.path.dirname(out),exist_ok=True);im.save(out)
    if changed: print(os.path.relpath(f,SRC),changed)
