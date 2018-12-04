import re, os, os.path, time, shutil
from urllib.request import urlretrieve
from pynput.mouse import Controller as mouseController
from pynput.mouse import Button
from pynput.keyboard import Controller as keyboardController
from pynput.keyboard import Key, Controller

pages = [
	# 'https://tr.pinterest.com/nota181161/%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5/?lp=true',
	# 'https://tr.pinterest.com/caraseggelke/crocheting/?lp=true',
	# 'https://tr.pinterest.com/hirokoshinkai2/%E3%81%8B%E3%81%8E%E9%87%9D%E7%B7%A8%E3%81%BF%E3%81%AE%E7%B8%81/?lp=true',
	# 'https://tr.pinterest.com/elizabethaffari/artesanatos/?lp=true',
	# 'https://tr.pinterest.com/oksana_dovshenko/%D0%BA%D1%80%D1%8E%D1%87%D0%BE%D0%BA/?lp=true',
	# 'https://tr.pinterest.com/tyschukgb/%D1%83%D0%B7%D0%BE%D1%80%D1%8B/?lp=true',
	# 'https://tr.pinterest.com/haticetavus/galeri/?lp=true',
	# 'https://tr.pinterest.com/lorenamarialista/crochet/?lp=true',
	# 'https://tr.pinterest.com/lianayaremenko/%D1%80%D0%BE%D0%BA%D0%BE%D0%BA%D0%BE/?lp=true',
	# 'https://tr.pinterest.com/mariadefatimaalvesmelo594/croch%C3%A9/?lp=true',
	# 'https://tr.pinterest.com/rabiaistanbul/%C3%B6rg%C3%BC-2/?lp=true',
	# 'https://tr.pinterest.com/jeislas/croch%C3%AA/?lp=true',
 #  'https://tr.pinterest.com/fatimamarasciul/squares/?lp=true',
 #  'https://tr.pinterest.com/sandrasdecesare/barrados/?lp=true',
  'https://tr.pinterest.com/omerdenur/dantel/?lp=true',
  'https://tr.pinterest.com/onopa_l/%D0%BA%D1%80%D1%8E%D1%87%D0%BE%D0%BA/?lp=true',
  'https://tr.pinterest.com/gizemtugba91/oya/?lp=true',
  'https://tr.pinterest.com/esmaatif72/dantel/?lp=true',
  'https://tr.pinterest.com/genypimentel/flores/?lp=true',
  'https://tr.pinterest.com/anamureira1497/colchas/?lp=true',
  'https://tr.pinterest.com/carol589sc/crochet-squares/?lp=true',
  'https://tr.pinterest.com/albenliserpil/denenecek-projeler/?lp=true',
  'https://tr.pinterest.com/hsf1510/croch%C3%AA/?lp=true',
  'https://tr.pinterest.com/ipelevina/%D0%B2%D1%8B%D1%88%D0%B8%D0%B2%D0%BA%D0%B0/?utm_campaign=rdboards&e_t=d90b79f739d04797afee25bfaa092e1a&utm_content=540854305189094101&utm_source=31&utm_term=12&utm_medium=2004',
  'https://tr.pinterest.com/matelena8533/dantela/?lp=true',
  'https://tr.pinterest.com/nit_torres/croch%C3%AA-fil%C3%A9/?lp=true',
  'https://tr.pinterest.com/toydemirg/arka-bah%C3%A7e-tavuk/?lp=true',
  'https://tr.pinterest.com/bretenluminita/flori/?lp=true',
  'https://tr.pinterest.com/elifsari4316/temizlik/?lp=true',
  'https://tr.pinterest.com/nih40gns/kenari/?lp=true',
  'https://tr.pinterest.com/ruksana7892/kitchen/?lp=true',
  'https://tr.pinterest.com/aynurkacaraksoy/p%C3%BCf-noktalar/?lp=true',
  'https://tr.pinterest.com/esmayildiz03/oya/?lp=true',
  'https://tr.pinterest.com/gaydaenko66/%D0%B2%D1%96%D0%B4%D0%B5%D0%BE/?lp=true',
  'https://tr.pinterest.com/mchlldemos/crafts/?lp=true',
  'https://tr.pinterest.com/etitiltan4499/%D7%AA%D7%97%D7%A8%D7%94-%D7%90%D7%99%D7%A8%D7%99%D7%AA-%D7%99%D7%95%D7%98%D7%99%D7%95%D7%91/?lp=true',
  'https://tr.pinterest.com/maristelape0208/pontos/?lp=true',
  'https://tr.pinterest.com/ninjaducky88/squares/?lp=true',
  'https://tr.pinterest.com/meralacik57/t%C4%B1%C4%9F-y%C3%BCn-%C3%B6rnekleri/?lp=true',
  'https://tr.pinterest.com/vikipitts/crochet/?lp=true',
  'https://tr.pinterest.com/ramirezplucy/crochet/?lp=true',
  'https://tr.pinterest.com/odorigon/croche/?lp=true',
  'https://tr.pinterest.com/debmomx4/blankies/?lp=true',
  'https://tr.pinterest.com/rukiyeserap/el-i%C5%9Fi/?lp=true',
	]

# myPath = "C:\\Users\\Raq\\Downloads\\"

def openFirefox(page):
    mouse = mouseController()
    keyboard = keyboardController()
    mouse.position = (10, 750)
    time.sleep(2)

    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

    keyboard.type('Firefox')
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    with keyboard.pressed(Key.ctrl):
        time.sleep(2)
        keyboard.press('l')
    time.sleep(2)

    keyboard.type(page)
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

    mouse.position = (10, 500)
    time.sleep(2)

    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)

    for i in range(60*20):
        keyboard.press(Key.page_down)
        time.sleep(1)

    with keyboard.pressed(Key.ctrl):
        keyboard.press('s')
    time.sleep(5)

    keyboard.type(page.split('/')[3] + '_' + page.split('/')[4] + '.html')
    time.sleep(5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)

def exitWideProgram():
    mouse = mouseController()
    mouse.position = (1360, 8)
    time.sleep(2)

    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(2)


DIR_PATH = 'C:\\Users\\Raq\\Desktop\\muhsine-edremit\\' 

for page in pages:
  try:
    openFirefox(page)
    PAGE_NAME = page.split('/')[3] + '_' + page.split('/')[4]
    count = 0
    library = []
    time.sleep(5)

    if not os.path.exists(DIR_PATH + PAGE_NAME):
      os.makedirs(DIR_PATH + PAGE_NAME)

    for i in str(open(DIR_PATH + PAGE_NAME + '.html', encoding="utf8").readlines()).split(" "):#str(requests.get(URL).text).split(" "):
      if re.findall('http.*\.jpg', i):
        try:
          current_img = re.findall('http.*\.jpg', i)[0]
          img_lib_name = current_img.split("/")[-1].split(".")[0]
          if img_lib_name not in library:
            count += 1
            library.append(img_lib_name)
            urlretrieve(current_img, os.path.join(DIR_PATH, "%s\\%s_%s.jpg" % (PAGE_NAME, PAGE_NAME, str(len(os.listdir(os.path.join(DIR_PATH, PAGE_NAME)))))))
        except:
          print("PASSED", i)
    os.remove(DIR_PATH + PAGE_NAME + '.html')
    shutil.rmtree(DIR_PATH + PAGE_NAME + '_files')
    exitWideProgram()
  except:
    print('Something went wrong on %s' % PAGE_NAME)