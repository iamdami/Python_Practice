from PIL import Image

# 이미지 객체로 생성 
im = Image.open(file_) 

# RGB 모드로 변경
rgb_im = im.convert('RGB') 

# 지정한 좌표(100, 100)의 색상을 r,g,b 변수에 넣음 
r, g, b = rgb_im.getpixel((100, 100)) 

print(r)
print(g)
print(b)
