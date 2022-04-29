from . import Pattern

# Languages

__english = "[a-zA-Z]+"
__english_label = "ENGLISH"
english = Pattern(__english, __english_label)

__french = "[a-zA-Zéàèùâêîôûçäëïüœÿ]+"
__french_label = "FRENCH"
french = Pattern(__french, __french_label)

__spanish = "[a-zA-Záéíóúñ]+"
__spanish_label = "SPANISH"
spanish = Pattern(__spanish, __spanish_label)

__arabic = "[\\u0600-\\u06FF]+"
__arabic_label = "ARABIC"
arabic = Pattern(__arabic, __arabic_label)

__hebrew = "[\\u0590-\\u05FF]+"
__hebrew_label = "HEBREW"
hebrew = Pattern(__hebrew, __hebrew_label)

__turkish = "[a-zA-ZğüşöçİĞÜŞÖÇ]+"
__turkish_label = "TURKISH"
turkish = Pattern(__turkish, __turkish_label)

__russian = "[\\u0621-\\u064A\\u0660-\\u0669]+"
__russian_label = "RUSSIAN"
russian = Pattern(__russian, __russian_label)

__german = "[a-zA-Z\\u00E4\\u00F6\\u00FC\\u00C4\\u00D6\\u00DC\\u00df]+"
__german_label = "GERMAN"
german = Pattern(__german, __german_label)

__chinese = "[\\u4e00-\\u9fa5]+"
__chinese_label = "CHINESE"
chinese = Pattern(__chinese, __chinese_label)

__greek = "[\\u3131-\\uD79D]+"
__greek_label = "GREEK"
greek = Pattern(__greek, __greek_label)

__japanese = "[\\u3041-\\u3096\\u30A0-\\u30FF\\u3400-\\u4DB5\\u4E00-\\u9FCB\\uF900-\\uFA6A\\u2E80-\\u2FD5\\uFF5F-\\uFF9F\\u3000-\\u303F\\u31F0-\\u31FF\\u3220-\\u3243\\u3280-\\u337F]+"
__japanese_label = "JAPANESE"
japanese = Pattern(__japanese, __japanese_label)

__hindi = "[\\u0900-\\u097F]+"
__hindi_label = "HINDI"
hindi = Pattern(__hindi, __hindi_label)

__bangali = "[\\u0980-\\u09FF]+"
__bangali_label = "BANGALI"
bangali = Pattern(__bangali, __bangali_label)

__armenian = "[\\u0530-\\u058F]+"
__armenian_label = "ARMENIAN"
armenian = Pattern(__armenian, __armenian_label)

__swedish = "[åäöÅÄÖA-Za-z]+"
__swedish_label = "SWEDISH"
swedish = Pattern(__swedish, __swedish_label)

__portoguese = "[a-zA-Záéíóúçâêôãõà]+"
__portoguese_label = "PORTOGUESE"
portoguese = Pattern(__portoguese, __portoguese_label)

__balinese = "[\\u1B00-\\u1B7F]+"
__balinese_label = "BALINESE"
balinese = Pattern(__balinese, __balinese_label)

__georgian = "[\\u10A0-\\u10FF]+"
__georgian_label = "GEORGIAN"
georgian = Pattern(__georgian, __georgian_label)
