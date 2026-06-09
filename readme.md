# Vypracované otázky ke státní závěrečné zkoušce
- obor: BPC-MET
- rok: 2026

## Podekovani
Repo vzniklo na zaklade podnetu od [kamarada z TLI](https://github.com/EmanuelAntol), ktery zpracoval otazky pro svuj obor v repozitari [zde](https://github.com/EmanuelAntol/SZZ-BPC-TLI-2026). Obdobne byly zpracovany [otazky pro EKT](https://github.com/Stredoslovak/SZZ-BPC-EKT-2026) dalsimi kolegy. Na tyto dva projekty repo volne navazuje.


## Otazky a obory
- ackoliv bylo repo vytvoreno pro rok 2026, otazky se dramaticky v prubehu let nemeni
- otazky byly vytvoreny pro obor BPC-MET (mikroelektronika), lze ale predpokladat, ze pro novy obor BPC-NPC (navrh cipu) budou nektere z otazek podobne

## Okruhy
### Aplikovana mikroelektronika a technologie
- [x] DIZ
- [ ] MTS
- [ ] NAO
- [x] NDI
- [ ] NRP
- [ ] OZU
- [ ] UIP  

### Zaklady mikroelektroniky a technologie
#### Skupina I
- [x] AEY
- [x] DIO
- [x] ESO

#### Skupina II
- [x] EMV1
- [x] EMV2
- [x] MPE

## Disclaimer
Původní motivací byl osobní souhrn otázek k SZZ pro MET. Díky snaze kolegů z TLI a EKT jsem se rozhodl své poznámky *(psané v programu Joplin)* také zveřejnit.
Vzhledem k širokému obsahu státnicových témat **nemělo smysl vypracovat otázky znovu**, namísto bylo využito již existujících zpracování, skript atp. Snahou bylo tyto zdroje citovat v patřičném md souboru.
Repozitář tedy není nutně autorským dílem, ale spíše kompilací vhodných zdrojů a poznámek z nich.

Snahou bylo také nezveřejňovat v plném rozsahu zdroje, jež jsou duševním vlastnictvím univerzity. Na takové zdroje je tedy odkázáno pouze tak, aby se k nim dostal student předmětu.

Některé další odkazy se mohou odkazovat na vlastní poznámky z jiných Joplin sešitů. Takové poznámky je možno uvést v `_resources`. Zatím jsem tak ale neudělal.

Jakékoliv poznámky úpravy nebo opravy jsou vítány:)

## Struktura repozitare
#### Pravidla strukturovani
1. pro kazdy okruh je vedena podslozka ve slozce `./text`
2. soucasti podslozky okruhu je soubor `_otazky.md` shrnujici soubor otazek okruhu a soubor `_zdroje a materialy.md` shrnujici zdroje pouzity behem vypracovani okruhu
3. kazda z otazek je popsana ve vlastnim markdown souboru, ktery je soucasti podslozky okruhu
4. obrazky a jine zdroje ci prilohy jsou soucasti slozky `./_resources`

#### Vycet souboru repozitare
- ke commitu `e23fadc92ca739f9c13f88920a4fa9bef127d7c5`
- Pozn.: vytvoreno prikazem `tree .`

```text
├── _resources
│   └── ...
└── text
    ├── AEY
    │   ├── 10. Spec integrovane zesilovace.md
    │   ├── 1. ZV.md
    │   ├── 2. OPA VFA.md
    │   ├── 3. OTA, CC,  CFA, TIA, diam trans,.md
    │   ├── 4. Filtry, deleni.md
    │   ├── 5. Filtry, aktivni.md
    │   ├── 6. RC oscilátory.md
    │   ├── 7. Komparatory, zavedeni hystereze.md
    │   ├── 8. Generátory s komparátory s hysterezí.md
    │   ├── 9. Operační usměrňovače.md
    │   ├── _otazky.md
    │   └── _zdroje a materialy.md
    ├── DIO
    │   ├── 1. Návrh v prostředí a ruční návrh.md
    │   ├── 2. Části struktury modelu VHDL.md
    │   ├── 3. Základní logická hradla.md
    │   ├── 4. Kombinacni obvody ve VHDL.md
    │   ├── 5. Sekvencni obvody ve VHDL.md
    │   ├── 6. Sekvencni obvody, casova analyza.md
    │   ├── 7. Sekvencni obvody, FSM.md
    │   ├── _otazky.md
    │   └── _zdroje a materialy.md
    ├── DIZ
    │   ├── 10. Zkoušky, klimatické a mechanické.md
    │   ├── 1. AFM.md
    │   ├── 2. Optická mikroskopie, světlé a tmavé pole.md
    │   ├── 3. Optická mikroskopie, hodnoty.md
    │   ├── 4. SEM, optika.md
    │   ├── 5. SEM, detekce.md
    │   ├── 6. E-beam, interakce.md
    │   ├── 7. Li-ion baterie.md
    │   ├── 8. Elchem zdroje.md
    │   ├── 9. Zkoušky bezpečnosti.md
    │   ├── _otazky.md
    │   └── _zdroje a materialy.md
    ├── EMV1
    │   ├── 10. Výroba waferu.md
    │   ├── 11. Výroba polovodičů.md
    │   ├── 1. Dielektrika a izolanty.md
    │   ├── 2. Azbest, slída, sklo.md
    │   ├── 3. Keramika.md
    │   ├── 4. Plasty.md
    │   ├── 5. Vodivé a odporové materiály.md
    │   ├── 6. Magnetismus.md
    │   ├── 7. Polovodičové materiály.md
    │   ├── 8. PN, teplotní nerovnováha.md
    │   ├── 9. PN přechod, MS přechod.md
    │   ├── _otazky.md
    │   └── _zdroje a materialy.md
    ├── EMV2
    │   ├── 10. Elektroerozivní procesy.md
    │   ├── 1. Povrchové úpravy.md
    │   ├── 2. Tenké vrstvy.md
    │   ├── 3. Montážní technologie.md
    │   ├── 4. Elektronové procesy.md
    │   ├── 5. Iontové procesy.md
    │   ├── 6. Rentgenové procesy.md
    │   ├── 7. Jaderné procesy.md
    │   ├── 8. Laserové procesy.md
    │   ├── 9. Ultraakustické procesy.md
    │   ├── _otazky.md
    │   └── _zdroje a materialy.md
    ├── ESO
    │   ├── 10. Fotoelektronika.md
    │   ├── 1. Prechod PN.md
    │   ├── 2. Dioda, charakteristika.md
    │   ├── 3. Dioda, dalsi typy.md
    │   ├── 4. BJT, charakteristika.md
    │   ├── 5. BJT, prurazy a modely.md
    │   ├── 6. BJT, zapojeni.md
    │   ├── 7. FET, typy a zapojeni.md
    │   ├── 8. FET, struktury, IGBT.md
    │   ├── 9. Spinaci prvky.md
    │   ├── _otazky.md
    │   ├── _otazky_rozepsane.md
    │   └── _zdroje a materialy.md
    ├── MPE
    │   ├── 1. Atomová stavba, vazby, krystaly, defekty.md
    │   ├── 2. Vodivé materiály.md
    │   ├── 3. Polovodiče I.md
    │   ├── 4. Polovodiče II.md
    │   ├── 5. Dielektrika.md
    │   ├── 6. Magnetické materiály.md
    │   ├── 7. DPS a pájky.md
    │   ├── _otazky.md
    │   └── _zdroje a materialy.md
    └── NDI
        ├── 1. Postup při návrhu.md
        ├── 2. Simulace.md
        ├── 3. Verifikace.md
        ├── 4. Základní aritmetické operace.md
        ├── 5. Statická časová analýza.md
        ├── _otazky.md
        └── _zdroje a materialy.md
```

