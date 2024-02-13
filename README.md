# Animēto pārejas efektu realizācijas lietotne Python valodā, izmantojot Pillow un Tkinter bibliotēkas

## Satura rādītājs

1. [Uzdevuma nostādne](#uzdevuma-nostādne)
2. [Tēmas teorētiskais apraksts](#tēmas-teorētiskais-apraksts)
3. [Izmantotās Bibliotēkas](#izmantotās-bibliotēkas)
4. [Iestatīšana un izpilde](#iestatīšana-un-izpilde)
5. [Izmantotie avoti](#izmantotie-avoti)

   
## Uzdevuma nostādne:
Realizēt lietotni, animēto pārejas efektu izveidei starp diviem attēliem.   
Jārealizē 3 pārejas efekti (Swipe, Curtain, Fade)

- Lietotājam jābūt iespējai atvērt divus jebkādus attēlus, izmantojot lietotāja saskarni
- Lietotnē paredzēt iespēju parādīt reāllaika animāciju izvēlēto divu attēlu pārejai
- Nedrīkst izmantot bibliotēkas pārejas realizācijai (pārejas algoritmi jāprogrammē pašiem) 


## Tēmas teorētiskais apraksts

Attēlu pārejas ir animācijai līdzīgi efekti, kas tiek parādīti slaidrādes skatā, pārvietojoties no viena attēlauz nākamo.

Pēc darba uzdevuma nostādnes, jārealizē 3 pārejas efekti (Swipe, Curtain, Fade), papildus tām, darbā tika realizētas vēl 2 pārejas efekti - Shape (Circle) un Snail.

Tālāk ir sniegts pārejas efektu algoritmu apraksts.
   
### 1. Swipe:   
Algoritma apraksts:   
- Swipe animācijas mērķis ir panākt vienmērīgu attēlu pāreju no pirmā attēla uz otro, līdz pirmā attēla pilnība tiek aizvietota ar otro attēlu. Algoritms izmanto pikseļu rindas kopēšanu no otra attēla uz pirmo no augšas, līdz pilnībā tiek aizpildīta pirmā attēla zona.   


### 2. Curtain:   
Algoritma apraksts:   
- Curtain animācija radīs efektu, it kā aizkars tiek paceļams vai nolaižams, atklājot otro attēlu zem tā. Algoritms izmanto pikseļu kolonnas kopēšanu no otra attēla uz pirmo, bet, atkarībā no Swipe pārejas algoritma, tas kopē pikseļus no centra uz abām pusēm (pa labi un pa kreisi), līdz pirmā attēla zona tiks pilnībā aizpildīta, veidojot efektu kā aizkars atveras.   


### 3. Fade:   
Algoritma apraksts:   
- Fade animācijas mērķis ir panākt pāreju no viena attēla uz otro, izmantojot pakāpenisku krāsas izblāznēšanu. Algoritms izmanto RGBA (Red, Green, Blue, Alpha) krāsu modeli un funkciju blend, pakāpeniski samazinot pirmā attēla krāsas intensitāti (Alpha) no 100% līdz 0%, lai radītu iegremdējošu fade efektu.   


### 4. Shape (Circle):   
Algoritma apraksts:   
- Shape animācijas mērķis ir radīt pāreju starp attēliem, izmantojot noteiktu formas, šajā darbā - apļa. Algoritms pakāpeniski palielina apļa radiusu, iet cauri visiem pikseļiem un nosaka, vai tie atrodas apļa iekšienē. Ja ir iekšienē, tad tiek veikta pāreja uz otru attēlu pikseļiem.   


### 5. Snail:   
Algoritma apraksts:  
- Snail animācijas mērķis ir radīt pāreju starp attēliem, izmantojot spirālveida kustību (atgādina gliemežvāku, kas savīt spirālē). Algoritms sadala attēlu zonās un pakāpeniski kustina gliemežvītināto ceļu pa šīm zonām, kopējot pikseļus no otra attēla, līdz pirmā attēla zona pilnībā tiek aizvietota ar otro attēlu.   

    
## Izmantotās Bibliotēkas

### `Tkinter`:

- Iemesls: `Tkinter` ir Python standarta bibliotēka GUI (grafiskā lietotāja saskarne) izveidei. To izmanto, lai radītu interaktīvas lietotnes un logus ar pogām, ievades laukiem, etiķetēm u.c.

- Darbības apraksts: `Tkinter` nodrošina visu nepieciešamo, lai izveidotu un apstrādātu GUI. Manā darbā, tas tiek izmantots, lai izveidotu galveno lietotnes logu, iestatītu loga izmērus, pievienotu pogas, etiķetes un citus vizuālos elementus, ka arī, lai atvērtu failu dialogu attēla izvēlei.

- Izmantošanas iespējas: `Tkinter` var tikt izmantots, lai izveidotu dažādas lietotnes, sākot no vienkāršiem logiem ar pogām līdz sarežģītākām interfeisa struktūrām. Tas piedāvā daudz dažādu interaktīvo elementu, piemēram, pogas, izvēlnes, ievades lauki, attēlu rādītājus utt. 

### `Pillow (PIL):`

- Iemesls: `Pillow` ir attēla apstrādes bibliotēka, kas ļauj Python attēliem veikt dažādus darbības, piemēram, atvērt, rediģēt, saglabāt un manipulēt attēla datiem.

- Darbības apraksts: `Pillow` bibliotēka tiek izmantota, lai iegūtu pilnu kontroli pār attēliem. Darbā tas bija izmantots, lai atvērtu attēlus no faila, mainītu to izmērus, veiktu grafiskus efektus un pārvērstu attēlus par formātiem, kas var tikt parādīti tkinter lietotāja saskarnē.

- Izmantošanas iespējas: `Pillow` piedāvā plašas iespējas attēlu apstrādei. To var izmantot, lai veiktu dažādas manipulācijas ar attēliem, piemēram, iegūt informāciju par attēlu, apvienot attēlus, mainīt attēlu izmērus, pārveidot krāsu režīmus, pielietot filtre un efektus, un daudzas citas funkcijas.
    
## Iestatīšana un izpilde

Pirms skriptu palaišanas pārliecinieties, ka jūsu sistēmā ir instalēts Python, Tkinter un Pillow bibliotēkas
1. Ja jums nav Python, varat to lejupielādēt no [Python oficiālās vietnes](https://www.python.org/downloads/).
2. Lejupielādējiet Tkinter:
   ```
   pip install tkinter
   ```
2. Lejupielādējiet Pillow:
   ```
   pip install pillow
   ```

   
## Izmantotie avoti

- Tkinter dokumentācija: https://docs.python.org/3/library/tkinter.html

- Pillow dokumentācija: https://pillow.readthedocs.io/en/stable/index.html   

- RTU DITF VDI Datorgrafikas un datorredzes katedras asoc. prof. Katrina Boločko, Dr.sc.ing. - Datorgrafikas un attēlu apstrādes pamati.

- Publikācija - Python Tkinter Tutorial: https://www.geeksforgeeks.org/python-tkinter-tutorial/

- ChatGPT: https://chat.openai.com/
