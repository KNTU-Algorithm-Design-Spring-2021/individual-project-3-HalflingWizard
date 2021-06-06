<div dir="rtl">

# جیمز باند - قسمت دوم
##### محمد نامورپور - 9920354
##### اسفند 99 - طراحی الگوریتم دکتر احمدی

<p align="center">
  <img src="https://s19.picofile.com/file/8435678950/Picture1.png" />
</p>

### فایل ها
فایل `james_bond.py` شامل تابع اصلی است که کار جدا کردن کلمات را انجام می دهد. دو راه برای استفاده از این تابع داریم. اول اینکه خودمان یک جمله بدهیم (به کمک `secret_decoder.py`) و دوم اینکه تعدادی کلمه از دیکشنری 3000 آکسفورد که من استفاده کرده ام، برداریم و یک جمله بسازیم و به تابع اصلی بدهیم. که این هم به کمک `test.py` انجام می شود
  
### روش کار
الگوریتم به صورت بازگشتی کار میکند. جمله را میگیرد، و از ابتدای آن شروع به جداسازی حروف میکند. هر کجا که حروف جدا شده یک کلمه تشکیل می دادند، آن بخش را جدا می کند و دوباره در ادامه جمله به دنبال کلمات می گردد. در این میان اگر در بخشی متوجه شود که در قسمت باقی مانده از جمله اش، کلمه ای نیست، باز میگردد و مجددا به جستجو می پردازد. 

### پیچیدگی برنامه
برای پیدا کردن پیچیدگی برنامه من از نوت بوک 
`test_bond.ipnb`
در کولب استفاده کردم. به کمک آن، از جملات 2 کلمه ای شروع کردم و یک بار، 10 جمله و یک بار دیگر، 100 جمله با تعداد کلمات مشخص به الگوریتم دادم. تعداد کلمات رفته رفته زیاد میشد تا آنجا که مثلا میانگین زمان صرف شده توسط الگوریتم به 10 یا 15 ثانیه برسد. سپس اینکه هر تعداد کلمه به طور میانگین چقدر طول کشیده تا توسط الگوریتم پردازش شود را بدست آوردم. حاصل این کار دو نمودار زیر است.
<p align="center">
  <img src="https://s19.picofile.com/file/8435729276/Picture1.png" />
</p>
<p align="center">
  <img src="https://s19.picofile.com/file/8435729292/Picture2.png" />
</p>
گفتنی است فایل `csv` مربوط به آنها نیز در فولدر `reports` وجود دارد.

ترندلاین های نزدیک به نمودار توسط اکسل رسم شد و براساس آن،
همانطور که مشخص است همیشه نمودار ما زیر خط `e^x` است پس میتوان گفت که این الگوریتم `O(2^n)` می باشد.
</div>
