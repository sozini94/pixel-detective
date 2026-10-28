from PIL import Image
from pathlib import Path
root=Path(__file__).resolve().parents[1]
src=Path(__file__).resolve().parents[2]/'픽셀 아트 추리 게임 에셋 시트(1).png'
im=Image.open(src).convert('RGBA')
rooms=['office','living','kitchen','alley']
for i,n in enumerate(rooms):
 x1=[20,398,775,1153][i];x2=[386,763,1141,1519][i]
 im.crop((x1,62,x2,352)).save(root/'assets/rooms'/f'{n}.png')
people=['office_worker','student','chef','shopkeeper','courier','guard','neighbor','mystery']
for i,n in enumerate(people):
 x1=20+i*189 if i<4 else 775+(i-4)*189
 # correct second row image x: 775 965 1151 1340
 x1=[20,205,393,585,775,965,1151,1340][i]
 x2=[194,382,574,764,954,1141,1329,1512][i]
 im.crop((x1,456,x2,630)).save(root/'assets/portraits'/f'{n}.png')
icons=['key','letter','cup','phone','laptop','cctv','memo','documents','wallet','cash','card','photo','knife','medicine','usb','box','receipt','glass','cigarettes','lighter','watch','cloth','gloves','footprint']
centers=[85,205,325,439,559,686,822,945,1077,1194,1316,1445]
for i,n in enumerate(icons):
 row=i//12;x=centers[i%12]; y=785 if row==0 else 914
 im.crop((max(0,x-52),y-45,min(1536,x+52),y+44)).save(root/'assets/icons'/f'{n}.png')
print('Cropped',len(rooms),'rooms,',len(people),'portraits,',len(icons),'icons')
