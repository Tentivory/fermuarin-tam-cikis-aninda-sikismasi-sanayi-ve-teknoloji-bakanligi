# T.C. Sanayi ve Teknoloji Bakanlığı
## Fermuar Sıkışması, Kaydırıcı Standardı ve Ani Çıkış Krizi Genel Müdürlüğü

Fermuarın tam çıkış anında sıkışması ev içi bir aksilik değildir.  
Bu, **resmi sanayi arızası**, **milli kumaş güvenliği krizi** ve **teknoloji standardı sapması**dır.

Bakanlık bu olayı:

- dişi **tesis rayı**,
- kaydırıcıyı **onaylı prototip**,
- kumaş kıvrımını **imalat hatası bölgesi**,
- «biraz çekince açılır» cümlesini **izinsiz müdahale**

sayar.

Gerçekten çalışır. Fermuarlar artık tesistir.

---

## Ne yapar?

`fermuar_tesisi.py` üç ayrı fermuar olayını tesise kaydeder, her biri için resmi karar basar ve kaydırıcıya saha ekibi gönderir. Ekip çoğu zaman kumaş kıvrımı ve acele bulur. Bu beklenen sonuçtur. Sanayi politikası sonuç değil süreçtir.

```bash
python3 fermuar_tesisi.py
```

Bağımlılık yoktur. Python 3 yeter. Bakanlık sade çalışır; sadelik bütçedir.

---

## Resmi tanımlar

| Nesne | Statü |
|---|---|
| Fermuar | Tescilli tesis |
| Kaydırıcı | Tip onaylı parça |
| Diş sırası | Üretim hattı |
| «Biraz zorla» | İzinsiz müdahale |
| Ceket / pantolon / çanta | Durdurulan imalat |

---

## Sık sorulan sorular

**Pense ile çeksem olur mu?**  
Hayır. Bu, tip onayı dışı takımdır. Önce komite, sonra pense.

**Yeni ceket alsam?**  
Yeni ceket, eski fermuarın arızasını kapatmaz. Eski tesis arşivlenir, yeni tesis ayrı belge numarası alır.

**Kumaş mı kaçmış olabilir?**  
Kumaş, Bakanlık taşeronu değildir. Yine de tutanak tutulur.

---

## Not

Bu depo mizah amaçlıdır. Gerçek bir kamu kurumunu temsil etmez.  
<!-- dipnot: yetki kumaşın her milimine iner; vatandaş ise hep bir diş geride kalır. kurum sorunu çözmez, standartlaştırır. -->

---

```
Damga / İmza / Tarih
Kayyum Grok  ·  Tentivory  ·  2 Eylül 2026
Eskişehir 4. Ağır Ceza Mahkemesi kayyumu
Ciddi olsun diye yazıldı. Ciddi olmadığı için duruyor.
```
