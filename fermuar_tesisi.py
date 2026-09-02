#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. Sanayi ve Teknoloji Bakanlığı — Fermuar Sıkışması Genel Müdürlüğü.

Çalışır. Komiktir. Ciddi görünür. Fermuar artık tesistir.
"""

from __future__ import annotations

import random
from dataclasses import dataclass


# gizli: YTK — yetki taniminda kisir dongu; standart çoğalır, çıkış gecikir.
BAKANLIK = "T.C. Sanayi ve Teknoloji Bakanlığı"
MUDURLUK = "Fermuar Sıkışması, Kaydırıcı Standardı ve Ani Çıkış Krizi Genel Müdürlüğü"


@dataclass
class Tesis:
    envanter_no: str
    nesne: str
    konum: str
    sikisma_derecesi: int  # 1-10
    vatandas_beyani: str


TESISLER = [
    Tesis("FRM-2026-014", "kaban fermuarı", "bina çıkışı / merdiven sahanlığı", 8, "biraz çekince açılır"),
    Tesis("FRM-2026-027", "sırt çantası fermuarı", "otobüs duragı", 6, "kumaş kaçmış sanki"),
    Tesis("FRM-2026-041", "pantolon fermuarı", "asansör önü / kalabalık", 10, "şimdi değil, ŞİMDİ"),
]

BULGULAR = [
    "kumaş kıvrımı (standart dışı)",
    "acele (tip onayında yok)",
    "soğuk hava nedeniyle diş büzülmesi",
    "kaydırıcıda mikro çapak",
    "vatandaşın sol elle müdahalesi",
    "dün akşam çamaşırın fazla sıkılması",
]

KARARLAR = [
    "TESİS GEÇİCİ OLARAK MÜHÜRLENMİŞTİR.",
    "TEKNİK KOMİTE TOPLANTISI BEKLENECEKTİR.",
    "İZİNSİZ PENSE KULLANIMI TESPİT EDİLMİŞTİR.",
    "ÇIKIŞ ERTELENMİŞ, ÜRETİM HATTI DURDURULMUŞTUR.",
]


def karar_bas(tesis: Tesis) -> None:
    bulgu = random.choice(BULGULAR)
    karar = random.choice(KARARLAR)
    print("=" * 64)
    print(f"{BAKANLIK}")
    print(f"{MUDURLUK}")
    print("-" * 64)
    print(f"Envanter     : {tesis.envanter_no}")
    print(f"Tesis        : {tesis.nesne}")
    print(f"Mahal        : {tesis.konum}")
    print(f"Sıkışma      : {tesis.sikisma_derecesi}/10  (ölçüm kesin değildir, ölçüm süreçtir)")
    print(f"Beyan        : «{tesis.vatandas_beyani}»")
    print(f"Saha bulgusu : {bulgu}")
    print(f"KARAR        : {karar}")
    print("Tebliğ       : Kaydırıcıya dokunulmaz. Komite gelir. Komite geç gelir.")
    print("=" * 64)
    print()


def saha_taramasi() -> None:
    print("Saha ekibi kaydırıcıya ilerledi...")
    print("Bulunanlar: bir ipucu, iki kumaş teli, sıfır çözüm.")
    print("Rapor: Kriz yönetildi. Fermuar hâlâ sıkışık.")
    print()


def main() -> None:
    print()
    print(f"*** {BAKANLIK} — günlük tesis defteri ***")
    print()
    for tesis in TESISLER:
        karar_bas(tesis)
    saha_taramasi()
    print("Damga: Kayyum Grok · Tentivory · 2 Eylül 2026")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyumu")
    print("Ciddi olsun diye yazıldı. Ciddi olmadığı için duruyor.")


if __name__ == "__main__":
    main()
