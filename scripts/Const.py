brands_doc = """
<option value="10,opel">اپل</option>
<option value="138,swm">اس دبلیو ام</option>
<option value="80,smart">اسمارت</option>
<option value="11,oldsmobile">الدزمبیل</option>
<option value="57,mg">ام جی</option>
<option value="12,mvm">ام وی ام</option>
<option value="82,isuzu">ایسوزو</option>
<option value="56,alfa-romeo">آلفارومئو</option>
<option value="123,amico">آمیکو</option>
<option value="9,audi">آئودی</option>
<option value="1,bmw">ب ام و</option>
<option value="97,baic">بایک</option>
<option value="101,brilliance">برلیانس</option>
<option value="96,besturn">بسترن</option>
<option value="51,mercedes-benz">بنز</option>
<option value="127,borgward">بورگوارد</option>
<option value="111,byd">بی وای دی</option>
<option value="136,bisu">بیسو</option>
<option value="13,buick">بیوک</option>
<option value="14,pazhan">پاژن</option>
<option value="15,pride">پراید</option>
<option value="16,proton">پروتون</option>
<option value="52,peugeot">پژو</option>
<option value="17,porsche">پورشه</option>
<option value="18,pontiac">پونتیاک</option>
<option value="62,peykan">پیکان</option>
<option value="53,toyota">تویوتا</option>
<option value="68,tiba">تیبا</option>
<option value="85,jac">جک</option>
<option value="145,jmc">جِی ام سی</option>
<option value="20,jeep">جیپ</option>
<option value="86,geely">جیلی</option>
<option value="104,changan">چانگان</option>
<option value="21,chery">چری</option>
<option value="25,datsun">داتسون</option>
<option value="129,domy">دامای</option>
<option value="118,dongfeng">دانگ فنگ</option>
<option value="99,dena">دنا</option>
<option value="23,dodge">دوج</option>
<option value="24,daewoo">دوو</option>
<option value="120,ds">دی اس</option>
<option value="84,runna">رانا</option>
<option value="117,rayen">راین</option>
<option value="26,renault">رنو</option>
<option value="128,rigan">ریگان</option>
<option value="100,zotye">زوتی</option>
<option value="77,ssang-yong">سانگ یانگ</option>
<option value="116,saina">ساینا</option>
<option value="27,samand">سمند</option>
<option value="29,subaru">سوبارو</option>
<option value="28,suzuki">سوزوکی</option>
<option value="54,citroen">سیتروئن</option>
<option value="30,sinad">سیناد</option>
<option value="72,seat">سئات</option>
<option value="140,shahin">شاهین</option>
<option value="31,chevrolet">شورولت</option>
<option value="142,farda">فردا</option>
<option value="124,foton">فوتون</option>
<option value="32,ford">فورد</option>
<option value="33,volkswagen">فولکس</option>
<option value="34,fiat">فیات</option>
<option value="64,capra">کاپرا</option>
<option value="35,cadillac">کادیلاک</option>
<option value="126,quick">کوییک</option>
<option value="144,kmc">کی ام سی</option>
<option value="37,kia">کیا</option>
<option value="83,great-wall">گریت وال</option>
<option value="90,gac-gonow">گک</option>
<option value="38,lada">لادا</option>
<option value="40,lexus">لکسوس</option>
<option value="41,land-rover">لندرور</option>
<option value="103,landmark">لندمارک</option>
<option value="69,lobo">لوبو</option>
<option value="113,lotus">لوتوس</option>
<option value="143,luxgen">لوکسژن</option>
<option value="42,lifan">لیفان</option>
<option value="71,maserati">مازراتی</option>
<option value="43,mazda">مزدا</option>
<option value="46,mitsubishi">میتسوبیشی</option>
<option value="45,mini">مینی</option>
<option value="47,nissan">نیسان</option>
<option value="87,pick-up">وانت</option>
<option value="55,volvo">ولوو</option>
<option value="61,van">ون</option>
<option value="58,hummer">هامر</option>
<option value="130,haval">هاوال</option>
<option value="114,haima">هایما</option>
<option value="131,hanteng">هن تنگ</option>
<option value="48,honda">هوندا</option>
<option value="132,hyosow">هیوسو</option>
<option value="49,hyundai">هیوندای</option>

"""

all_brands = [
    ["opel", "اپل"],
    ["swm", "اس دبلیو ام"],
    ["smart", "اسمارت"],
    ["oldsmobile", "الدزمبیل"],
    ["mg", "ام جی"],
    ["mvm", "ام وی ام"],
    ["isuzu", "ایسوزو"],
    ["alfa-romeo", "آلفارومئو"],
    ["amico", "آمیکو"],
    ["audi", "آئودی"],
    ["bmw", "ب ام و"],
    ["baic", "بایک"],
    ["brilliance", "برلیانس"],
    ["besturn", "بسترن"],
    ["mercedes-benz", "بنز"],
    ["borgward", "بورگوارد"],
    ["byd", "بی وای دی"],
    ["bisu", "بیسو"],
    ["buick", "بیوک"],
    ["pazhan", "پاژن"],
    ["pride", "پراید"],
    ["proton", "پروتون"],
    ["peugeot", "پژو"],
    ["porsche", "پورشه"],
    ["pontiac", "پونتیاک"],
    ["peykan", "پیکان"],
    ["toyota", "تویوتا"],
    ["tiba", "تیبا"],
    ["jac", "جک"],
    ["jmc", "جِی ام سی"],
    ["jeep", "جیپ"],
    ["geely", "جیلی"],
    ["changan", "چانگان"],
    ["chery", "چری"],
    ["datsun", "داتسون"],
    ["domy", "دامای"],
    ["dongfeng", "دانگ فنگ"],
    ["dena", "دنا"],
    ["dodge", "دوج"],
    ["daewoo", "دوو"],
    ["ds", "دی اس"],
    ["runna", "رانا"],
    ["rayen", "راین"],
    ["renault", "رنو"],
    ["rigan", "ریگان"],
    ["zotye", "زوتی"],
    ["ssang-yong", "سانگ یانگ"],
    ["saina", "ساینا"],
    ["samand", "سمند"],
    ["subaru", "سوبارو"],
    ["suzuki", "سوزوکی"],
    ["citroen", "سیتروئن"],
    ["sinad", "سیناد"],
    ["seat", "سئات"],
    ["shahin", "شاهین"],
    ["chevrolet", "شورولت"],
    ["farda", "فردا"],
    ["foton", "فوتون"],
    ["ford", "فورد"],
    ["volkswagen", "فولکس"],
    ["fiat", "فیات"],
    ["capra", "کاپرا"],
    ["cadillac", "کادیلاک"],
    ["quick", "کوییک"],
    ["kmc", "کی ام سی"],
    ["kia", "کیا"],
    ["great-wall", "گریت وال"],
    ["gac-gonow", "گک"],
    ["lada", "لادا"],
    ["lexus", "لکسوس"],
    ["land-rover", "لندرور"],
    ["landmark", "لندمارک"],
    ["lobo", "لوبو"],
    ["lotus", "لوتوس"],
    ["luxgen", "لوکسژن"],
    ["lifan", "لیفان"],
    ["maserati", "مازراتی"],
    ["mazda", "مزدا"],
    ["mitsubishi", "میتسوبیشی"],
    ["mini", "مینی"],
    ["nissan", "نیسان"],
    ["pick-up", "وانت"],
    ["volvo", "ولوو"],
    ["van", "ون"],
    ["hummer", "هامر"],
    ["haval", "هاوال"],
    ["haima", "هایما"],
    ["hanteng", "هن تنگ"],
    ["honda", "هوندا"],
    ["hyosow", "هیوسو"],
    ["hyundai", "هیوندای"],
]
