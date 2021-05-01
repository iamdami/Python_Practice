from PIL import Image, ImageDraw

img= Image.open("./img.jpg")
rgb_im = img.convert('RGB') 
logo = Image.open("/home/logo.jpg")

# template 이미지 객체 200, 200 위치에 logo 이미지 붙이기
rgb_im.paste(logo, (200, 200)) 

# 붙인 이미지를 새로운 이름으로 저장
rgb_im.save("./logo.jpg", "JPEG")
