import csv
import json
import re

raw = """Jakarta Utara - Batavia PIK	Rukan Golf Island Blok C No.36, Pantai Indah Kapuk, Jakarta Utara	0822-9999-5125	09.00-17.00  	https://share.google/IpaWoV3Os0TJKfkiO
Jakarta Utara - Kelapa Gading	LC6 / 38, Jl. Boulevard Bar. Raya No.53, Klp. Gading Bar. Jkt Utara, Daerah Khusus Ibukota Jakarta 14240	"0822 9999 5041\n"	09.00-20.00	https://maps.app.goo.gl/LR7QwFrddC56iQuH6
Jakarta Utara - Sunter	Metro Sunter Plaza, Jl. Danau Sunter Utara No.10, RT.10/RW.4, Papanggo, Kec. Tj. Priok, Jkt Utara, Daerah Khusus Ibukota Jakarta 14350	0811-1927-9993	10.00-21.00	https://maps.app.goo.gl/6R7YnKXGSY1QP3eU6
Jakarta Utara - ITC Mangga Dua	"ITC Mangga Dua, Lantai 5 Blok Iris No.23, Jkt Utara, Daerah Khusus Ibukota Jakarta 14430\n"	0822 9999 5064	10.00-18.00	https://maps.app.goo.gl/bKXgu23Tore59Jaj9
"Jakarta Selatan - Pondok Indah\n"	"Jl. Metro Pondok Indah No.161 Blok Tb27, Pd. Pinang, Kec. Kby. Lama, akarta Selatan,  12310\n"	 0822 9999 5034	09.00-20.00	https://maps.app.goo.gl/UVR87ToeQRZxcKL3A
Jakarta Selatan - Plaza Melawai Blok M	"Melawai Plaza, Jl. Melawai Raya.13 18, Blok T No.264 Lantai 1, Melawai, Kec. Kby. Baru, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12160\n"	0822 9999 5127	10.00-19.00	https://maps.app.goo.gl/t2riFzojWaqqrrFZ6
Jakarta Selatan - Pejaten	"Jl. Warung Jati Barat, RT.1/RW.5, Jati Padang, Ps. Minggu, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12540\n\n"	0822 9999 5029	10.00-22.00	https://maps.app.goo.gl/d26ezro6zm9e4ebQ8
Jakarta Selatan - Mall Ambassador Kuningan	"Mall Ambasador Kuningan - Jakarta Selatan (Lantai Dasar No.56 Patokan dekat dengan Pintu Timur sebelah ATM BCA )\n\n\n"	0822-9999-5031	10.00-21.00	https://maps.app.goo.gl/mZWK1xk41pMEipbj8
Jakarta Selatan - Mall Kalibata City	"Mal Kalibata City Square lantai dasar No. 1160 (Disebelah Gramedia)\n"	0811-1928-9994	10.00-22.00	https://maps.app.goo.gl/5EFSgp5kmHixus4R9
"Jakarta Selatan - Mall Fx Sudirman\n"	"Mall FX Sudirman, Lt.F4 No.19, Jakarta Pusat\n"	0822-9999-6027	10.00-22.00	https://maps.app.goo.gl/uxbYYm1mmyR3kyGj8
"Jakarta Selatan - Blok M Square\n"	"Blok M Square Lantai UG Blok A No.103 (Patokannya sebelah kartika gold)\n\n"	0822 9999 6153	10.00-20.00	https://maps.app.goo.gl/hnDQFSchLowW7Sn29
Jakarta Pusat - Petojo	"Jl. Petojo Melintang No.26A, Petojo Sel., Kecamatan Gambir, Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10160\n \n\n"	 0822-8283-9999	09.00-20.00	https://maps.app.goo.gl/ERmZ736w3fJfp8eU9
Jakarta Pusat - Cikini	"Cikini Gold Center Lt. UG.17, Jl. Pegangsaan Timur No.1, RT.1/RW.1, Menteng, Jakarta 10310\n"	021-21232275	09.00-17.00	https://maps.app.goo.gl/bdUzzNJJmxRrPNH9A
"Jakarta Pusat - Cikini 2\n"	"Cikini Gold Center Lantai GF 25-26, Jl. Pegangsaan Timur No.1, RT.1/RW.1,  Kota Jakarta Pusat, Daerah Khusus Ibukota Jakarta 10310\n"	0822-9999-4248	09.00-17.00	https://maps.app.goo.gl/7ZW65hmMnKsV7vDy5
Jakarta Barat - Cengkareng	"Ruko Sedayu Square, Jalan Kamal Raya Outer Ring Road No.H08, Cengkareng Bar., Kecamatan Cengkareng, Kota Jakarta Barat, Daerah Khusus Ibukota Jakarta 11730\n\n"	"Telephone: 021-52392506\nHp & Whatsapp: 0822-9999-7763"	09.00-20.00	https://maps.app.goo.gl/3r317hxAaFFe162U9
Jakarta Barat - Mall Ciputra Grogol	"Mall Ciputra, Lantai 1 No.42, Jl. Letjen S. Parman, RT.11/RW.1, Tj. Duren Utara, Kec. Grogol petamburan, Kota Jakarta Barat, DKI Jakarta\n\n\n"	0822 9999 5032	10.00-22.00	https://maps.app.goo.gl/HdK1w4BquY4zVH3aA
Jakarta Timur - PGC	"Mall PGC Cililitan, Lantai 2 Zona Biru No. 02 NM (Dekat Layanan Terpadu), Jl. Mayjen Sutoyo, Cililitan, Kec. Kramat Jati, Jakarta Timur, Daerah Khusus Ibukota Jakarta, 13640\n\n\n"	0811-1927-9995	10.00-22.00	https://maps.app.goo.gl/BetxccoZXPYVBkjP8
Depok - ITC Depok	"TC Depok, Samping Terminal Terpadu Gedoran Depok, LT.dasar Blok C5, Jl. Margonda No.56, Depok, Kec. Pancoran Mas, Kota Depok, Jawa Barat 16431\n"	0822-8283-9999	10.00-20.00	https://maps.app.goo.gl/Fm46LvXvkWs6PVKy7
Depok - Mall Cinere	"Mal Cinere, Lantai 1 unit 34 A, Jl. Cinere Raya No.1, Pangkalan Jati, Kec. Cinere, Kota Depok, Jawa Barat 16514\n\n"	0822-9999-5062	10.00-21.00	https://maps.app.goo.gl/X29YPtxnAY511Ueg8
Bekasi - Mega Bekasi Hypermall	"Mega Bekasi Hypermall,Lt.UG.133, Jl. Ahmad Yani No.1, RT.004/RW.001, Marga Jaya, Kota Bks, Jawa Barat 17141\n\n\n"	0822-9999-3167	10.00-20.00	https://maps.app.goo.gl/RfJfSHcENBnj5uA29
Bekasi - Cibubur	"Plasa Cibubur Lt.1 No.19.,\nJl. Transyogi, RT.001/RW.003, Jatikarya, Kec. Jatisampurna, Kota Bks, Jawa Barat 17435\n\n\n\n"	0822-9999-5026	10.00-21.00	https://maps.app.goo.gl/5oeWD4bV1Sc3Jq2m6
Bekasi - Harapan Indah	"Ruko Commersial Park, Jl Raya Harapan Indah, Pejuang, Kec Medan Satria, Kota Bekasi.\n\n"	0822 9999 6831	10.00-20.00	https://maps.app.goo.gl/q3xJTdEBCeqpHY5Q7
"Kabupaten Bekasi - Aeon Mall Deltamas Cikarang\n"	"AEON Mall Deltamas, Jl. Ganesha Boulevard No.123 B Lantai 1, Hegarmukti, Kec. Cikarang Pusat, Kabupaten Bekasi, Jawa Barat 17530\n\n"	0811-1928-9991	10.00-22.00	https://maps.app.goo.gl/LBYcQhwcqdRSyKk88
Kabupaten Bekasi - Grand Wisata Bekasi	"Ruko Rivertown Boulevard, Jl. Grand Wisata No.16 Blok BA02, Lambangsari, Kec. Tambun Sel., Kabupaten Bekasi, Jawa Barat 17510\n\n"	0822-9999-6184	10.00-22.00	https://maps.app.goo.gl/Uk52WmgYGaLHJFca9
Karawang 	"KCP Mall Karawang – Lantai GF No. A6 (Masuk dari Lobby Timur, di depan Optik Melawai)\n\n"	0822-9999-6147	10.00-22.00	https://maps.app.goo.gl/i6DnDafPKCiL6Byq8
Tangerang-Aeropolis	ruko apartemen, Aeropolis Commercial Park 2 A2. GT.06, Jl. Aeropolis, RT.004/RW.008, Neglasari, Kec. Neglasari, Kota Tangerang, Banten 15129	0822-9999-6124	10.00-18.00	https://maps.app.goo.gl/ABRbBWwWYjs5Xuyx6
Tangerang-Tangcity Mall	Tangcity Mall, Jl. Jenderal Sudirman.1 Lantai LG D-09, Cikokol, Kec. Tangerang, Banten 15117	0822-9999-4127	10.00-21.30	https://maps.app.goo.gl/1cERbFH4oSDXbCyk8
Tangerang-Tangcity Mall 2	Tangcity Mall, Ruko Business Park E38, (patokannya dekat dengan indomaret tangcity)	0822 9999 6157	10.00-20.00	https://maps.app.goo.gl/TNFfDhFTZQu4kdzX8
Tangerang Selatan- Mall ITC BSD	Mall ITC BSD Tangsel, Jl. Pahlawan Seribu No.12 LT. Dasar Blok C3 No.3A-5, Lengkong Wetan, Kec. Serpong, tangerang, Banten 15310	0822-9999-3248	10.00-20.00	https://maps.app.goo.gl/mz5PYvYNkHunNiGi9
Tangerang Selatan- Gading Serpong	Jl. Raya Kelapa Gading Utara, Ruko Fluoride, No.75, Gading Serpong, Tangerang	0822 9999 5074	10.00-20.00	https://maps.app.goo.gl/YLDTEU2nmrcC3gK99
Tangerang Selatan - Pasar Modern Bintaro	Pasar Modern Bintaro Jaya, Pd. Jaya, Kec. Pd. Aren, Kota Tangerang Selatan, Banten 15220	82299995039	09.00-20.00 	https://maps.app.goo.gl/jiRnQqhJMQ12Qfvr8
Tangerang Selatan - Pamulang	Jl.Pajajaran No.9 pamulang, Kota Tangerang Selatan, Banten	82299996083	10.00-20.00 	https://maps.app.goo.gl/UWr6fHBHKZSg4J9D7
Serang	Jl. Mayor Safei No.13, Kotabaru, Kec. Serang, Kota Serang, Banten 42112 (Patokan depan rumah tahanan klas 2B serang)	0822 9999 6150	10.00-20.00 	https://share.google/he28oGNWpc4764xyh
Cibinong	Jl Raya Bogor No. 320 KM 45, Cibinong, Kec Cibinong, Kab Bogor, Jawa Barat	0822 9999 6835	10.00-20.00 	https://share.google/ynBZdyPZ2rfyeLx2q
Bogor	Pasar Kebon Kembang, Blok F Trade Center Pasar Kebon Kembang Lantai Dasar No.194, Paledang, Bogor Tengah, Kota Bogor, Jawa Barat 16122	0822 9999 5076	09.00-17.00 	https://maps.app.goo.gl/1hw2wjGZezPq9Nz36
Bogor- Surya Kencana	Jl.Suryakencana, RT.01/RW.05, Gudang, Kecamatan Bogor Tengah, Kota Bogor, Jawa Barat 16131	0822-9999-5071	10.00-20.00 	https://maps.app.goo.gl/FhfQuQ7adeGKMacW9
Bandung-Kopo	Jl. Raya Kopo No.632, Babakan Ciparay, Kec. Babakan Ciparay, Kota Bandung, Jawa Barat 40225	0822 9999 5042	10.00-20.00 	https://maps.app.goo.gl/miB5sYDtJEu9MSiX7
Bandung-Sukajadi	"Jl. Sukajadi No.158, Cipedes, Kel. Pasteur, Kec. Sukajadi, Kota Bandung, Jawa Barat 40162\n\n"	0822-9999-7764	10.00-20.00 	https://maps.app.goo.gl/QtmLcyarVXytSMf67
Bandung-Otista	Jl. Otto Iskandar Dinata No.313, Balonggede, Kec. Regol, Kota Bandung, Jawa Barat 40251	0822-9999-5075	10.00-20.00	https://maps.app.goo.gl/s1QLWquckq4Q1YUw5
Cirebon	Jl. DR. Cipto Mangunkusumo No.53, Pekiringan, Kec. Kesambi, Kota Cirebon, Jawa Barat 45131	0822-9999-6042	10.00-20.00	https://maps.app.goo.gl/ddFUSGkiTYgaAc4k9
Surabaya- Pakuwon	Store kedua ada di PTC, Pakuwon Trade Center Mall Surabaya D2- 06 lt GF, Jl. Raya Lontar No.2 Lantai LG, Unit B6-09&10, Babatan, Kec. Wiyung, Surabaya, Jawa Timur 60123	"Lt GF, Surabaya, Jawa Timur 60123\nHp & Whatsapp: 0822-9999-4123\nLt.LG No.09-10\nHp & Whatsapp : 0822 9999 6173\n"	10.00-21.30	https://maps.app.goo.gl/TaRdoEw91ZPAPHZL8
Surabaya 2	Jl. Bubutan No.Kav D, Alun-alun Contong, Kec. Bubutan, Surabaya, Jawa Timur 60174	 0822-8283-9999	10.00-20.00	https://maps.app.goo.gl/Kf8ThALF4BzAmr6u6
Surabaya 3	Royal Plaza, Jl. Ahmad Yani No.16-18, Wonokromo, Kec. Wonokromo, Surabaya, Jawa Timur 60243	 0822 99996048	10.00-22.00	https://maps.app.goo.gl/EXrRVKpfSEKok81x5
Malang	Jl. S.W. Pranoto No. 2H, Sukoharjo – Klojen, Malang	0822-9999-6145	10.00-20.00	https://maps.app.goo.gl/JjGCvFJRjGfw4CHT9
Semarang	Jl. K.H. Wahid Hasyim Jl. Kranggan Dalam No.97, Bangunharjo, Kec. Semarang Tengah, Kota Semarang, Jawa Tengah 50139	81119289992	09.00-20.00	https://maps.app.goo.gl/8cWRLR4Znr55mLkh
Semarang 2	Ruko Jl. Pandanaran No.kav.6, Pekunden, Kec. Semarang Tengah, Kota Semarang, Jawa Tengah 50134	0822 9999 6170	10.00-20.00	https://maps.app.goo.gl/8bHxfXkAffkXPHMF6
Yogyakarta - Plaza Malioboro	Plaza Malioboro, Jl. Malioboro No.52-58 Lantai UG, Suryatmajan, Kec. Danurejan, Kota Yogyakarta, Daerah Istimewa Yogyakarta 55213	81119719996	"Senin-jumat 10:00-22:00\nSabtu-minggu 09:00-22:00"	https://maps.app.goo.gl/jHdFX3r3g4wNM3VX7
"Yogyakarta - Sleman\n"	Jl. Laksda Adisucipto No.1, Papringan, Caturtunggal, Kec. Depok, Kabupaten Sleman, Daerah Istimewa Yogyakarta 55281	 0822 9999 6038	10.00-20.00	https://maps.app.goo.gl/PNCEiQ1Muf55zu7A7
Lamongan	"Jl. DR. Wahidin No.17, Tumenggungan, Kec. Lamongan, Kabupaten Lamongan, Jawa Timur 62214\n\n\n"	0822-9999-6081	10.00-20.00	https://maps.app.goo.gl/QWRDKRZ34qfkSdBw5
Solo - Pakuwon Mall Solo	"Pakuwon Mall Solo Baru, Jl. Ir. Soekarno, Dusun II, Madegondo, Kec. Grogol, Kabupaten Sukoharjo, Jawa Tengah 57552\n"	0822 9999 6047	10.00-22.00	https://maps.app.goo.gl/VLQT7gxCwT4EWcry9
Madura	"Jl. Trunojoyo No.37, Pejagan, Kec. Bangkalan (di sebrang toko cat, sebelah toko Belikopi)\n\n\n"	0822-9999-6043	10.00-20.00	https://maps.app.goo.gl/a6E4KdziGhFJxS8u6
Medan - Medan Mall	"Medan Mall, Jl. M. T. Haryono No.21 Lt Dasar, Pusat Ps., Kec. Medan Kota, Kota Medan, Sumatera Utara 20212\n\n\n"	0822-9999-3238	09.00-20.00	https://maps.app.goo.gl/awrqbL2wqq3gRmxB6
Palembang	"Jl. Letkol Iskandar No.27 A, B, C, 24 Ilir, Kec. Bukit Kecil, Kota Palembang, Sumatera Selatan 30113\n"	82299996073	10.00-20.00	https://maps.app.goo.gl/RQTRMqK9dKFt3GB98
Jambi	"Pert. Glodok Makmur 27 C, Jl. Hayam Wuruk No.11180 Lt. Dasar, Jelutung, Jambi, Kota Jambi, Jambi 36124\n"	0822 9999 6825	10.00-20.00	https://maps.app.goo.gl/RQTRMqK9dKFt3GB98
Bengkulu	"Jl Soeprapto No 4, Pengantungan, Kec Ratu Samban, Kota Bengkulu, Bengkulu\n\n\n"	0822 9999 6836	10.00-20.00	https://maps.app.goo.gl/CTDFakP5m2k5CP4XA
Lampung	Jl. Jendral Sudirman, Kel/Kec. Enggal, kota bandar Lampung (Samping BRI)	0822 9999 6082	10.00-20.00	https://maps.app.goo.gl/hS29QFZSHjj3Q3b26
Bali- Denpasar	Jl. Hasanuddin No.54, Dauh Puri Kangin, Kec. Denpasar Bar., Kota Denpasar, Bali 80232	0822-9999-3136	10.00-20.00 WITA	https://maps.app.goo.gl/Z2XnkkL92WoUL5qv6
Lubuk Linggau	Jl YOS Sudarso No 291 Kel Taba Jemekah Kec Lubuk Linggau Timur 1 ( Patokan Pom Bensin Sebelah Indomaret)	0822 9999 6827	10.00-20.00  	https://maps.app.goo.gl/VeyEwu96wQSLJMmf7
Bali Outlet 2	L.Gn.Soputan No 11E, Pemecutan Klod, Kota Denpasar, Bali (Patokannya samping sego sambel)	0822 9999 6037	10.00-20.00 WITA	https://share.google/0l2Kn2F2j4DwaXkkd
Medan - Medan Centre Point	Alamat : Lantai 3 No. 19 Mall Centre Point Medan, Jl. Jawa No. 8 Medan, Kel. Gg buntu, kec. Medan Timur - SUMUT	0822 9999 6852	10.00-20.00  	https://maps.app.goo.gl/zTS4kNTUWjHyVY2B9
Medan - Plaza Medan Fair	Plaza Medan Fair, Jl. Gatot Subroto No.30 Lantai 1, Sekip, Kec. Medan Petisah, Kota Medan, Sulawesi Utara 20113	0822 9999 7048	10.00-22.00	https://maps.app.goo.gl/cDAuHmeetjXc56qA6
Riau - Pekanbaru	Jl. Tuanku Tambusai No.223, Wonorejo, Kec. Marpoyan Damai, Kota Pekanbaru, Riau 28125	0822-9999-6854	10.00-22.00	https://maps.app.goo.gl/xkDyixXUrDZTu5m28
Aceh - Banda Aceh	"Jl. Sri Ratu Syafiatuddin No.4, Banda Aceh City, Aceh ( Patokan Dekat Kodam Iskandar Muda )\n"	0822 9999 7092	10.00-20.00	https://maps.app.goo.gl/Weog7Fv7AnrgnQgs7
Tangerang - Citra Raya	Patokan Samping BRI, Ruko Grand Boulevard, Jl. Citra Raya Boulevard No.10 Blok D 1, Ciakar, Kec. Cikupa, Kabupaten Tangerang, Banten 15610	0822 9999 7105	10.00-20.00	https://maps.app.goo.gl/T6wWhkkqrEmQ3f1i9
Serang - Cikande	"Jl. Raya Serang km 27, Cikande, Serang Banten (Sebrang Koramil Cikande/Samping Sorum Yamaha) \n"	0822-9999-7065	10.00-18.00  	https://maps.app.goo.gl/HXAA265SwCgTREBE9
Rangkas	Jl. Rt Hardiwinangun No.45, Muara Ciujung Bar., Kec. Rangkasbitung, Kabupaten Lebak, Banten 42312	0822-9999-7052	10.00-18.00  	https://maps.app.goo.gl/PGZM6HBNxeKpCM9V7
Lombok	"Jl. Pejanggik No.8, Cakranegara Bar., Kec. Cakranegara, Mataram, Lombok, Nusa Tenggara Bar. 83231\n\n\n"	 0822-9999-3018	10.00-18.00 WITA	https://maps.app.goo.gl/5eK6qS4aLY6AdfqG6
Makasar	"Ruko Ruby, Jl. Boulevard No.26, Masale, Kec. Panakkukang, Kota Makassar, Sulawesi Selatan 90222\n"	0822-9999-6126	10.00-20.00 WITA	https://maps.app.goo.gl/4Dg5eeQqbGJpXK8w9"""

import io

stores = []
reader = csv.reader(io.StringIO(raw.replace('\\n', '\n')), delimiter='\t', quotechar='"')
for i, row in enumerate(reader):
    if len(row) >= 5:
        stores.append({
            "id": f"st-{i+1}",
            "name": row[0].strip(),
            "address": row[1].strip(),
            "phone": row[2].strip(),
            "hours": row[3].strip(),
            "note": "BUKA SETIAP HARI",
            "mapCoordinates": row[4].strip()
        })

with open('data/siteData.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

data['stores'] = stores

with open('data/siteData.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully updated to {len(stores)} stores.")
