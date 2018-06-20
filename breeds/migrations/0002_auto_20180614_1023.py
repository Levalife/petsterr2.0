# Generated by Django 2.0.6 on 2018-06-14 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='title',
            field=models.CharField(blank=True, choices=[('affenpinscher', 'Affenpinscher'), ('afghan_hound', 'Afghan Hound'), ('atlas_mountain_dog', 'Atlas Mountain Dog'), ('airedale_terrier', 'Airedale Terrier'), ('akita', 'Akita'), ('alaskan_malamute', 'Alaskan Malamute'), ('alpine_dachsbracke', 'Alpine Dachsbracke'), ('american_akita', 'American Akita'), ('american_cocker_spaniel', 'American Cocker Spaniel'), ('american_foxhound', 'American Foxhound'), ('american_staffordshire_terrier', 'American Staffordshire Terrier'), ('american_water_spaniel', 'American Water Spaniel'), ('medium-sized_anglo-french_hound', 'Medium-sized Anglo-French Hound'), ('appenzell_cattle_dog', 'Appenzell Cattle Dog'), ('ariege_hound', 'Ariege Hound'), ('australian_cattle_dog', 'Australian Cattle Dog'), ('australian_kelpie', 'Australian Kelpie'), ('australian_shepherd', 'Australian Shepherd'), ('australian_silky_terrier', 'Australian Silky Terrier'), ('australian_stumpy_tail_cattle_dog', 'Australian Stumpy Tail Cattle Dog'), ('australian_terrier', 'Australian Terrier'), ('azawakh', 'Azawakh'), ('french_water_dog', 'French Water Dog'), ('basenji', 'Basenji'), ('artesian-norman_basset', 'Artesian-Norman Basset'), ('blue_gascony_basset', 'Blue Gascony Basset'), ('fawn_brittany_basset', 'Fawn Brittany Basset'), ('basset_hound', 'Basset Hound'), ('bavarian_mountain_scenthound', 'Bavarian Mountain Scenthound'), ('beagle', 'Beagle'), ('beagle-harrier', 'Beagle-Harrier'), ('bearded_collie', 'Bearded Collie'), ('bedlington_terrier', 'Bedlington Terrier'), ('white_swiss_shepherd_dog', 'White Swiss Shepherd Dog'), ('beauceron', 'Beauceron'), ('briard', 'Briard'), ('picardy_sheepdog', 'Picardy Sheepdog'), ('bernese_mountain_dog', 'Bernese Mountain Dog'), ('bichon_frise', 'Bichon Frise'), ('havanese', 'Havanese'), ('billy', 'Billy'), ('black-and-tan_coonhound', 'Black-and-Tan Coonhound'), ('bolognese', 'Bolognese'), ('border_collie', 'Border Collie'), ('border_terrier', 'Border Terrier'), ('bosnian_coarsehaired_hound', 'Bosnian Coarsehaired Hound'), ('boston_terrier', 'Boston Terrier'), ('french_bulldog', 'French Bulldog'), ('bouvier_des_ardennes', 'Bouvier des Ardennes'), ('bouvier_des_flandres', 'Bouvier des Flandres'), ('italian_pointer', 'Italian Pointer'), ('austrian_black-and-tan_hound', 'Austrian Black-and-Tan Hound'), ('ariege_pointer', 'Ariege Pointer'), ('auvergne_pointer', 'Auvergne Pointer'), ('bourbonnais_pointer', 'Bourbonnais Pointer'), ('french_pointer)_gascogne_type_(large)', 'French Pointer, Gascogne type (Large)'), ('french_pointer)_pyrenean_type_(small)', 'French Pointer, Pyrenean type (Small)'), ('saint-germain_pointer', 'Saint-Germain Pointer'), ('medium_griffon_vendeen', 'Medium Griffon Vendeen'), ('broholmer', 'Broholmer'), ('bull_terrier', 'Bull Terrier'), ('bulldog', 'Bulldog'), ('bullmastiff', 'Bullmastiff'), ('majorca_shepherd_dog', 'Majorca Shepherd Dog'), ('majorca_mastiff', 'Majorca Mastiff'), ('cairn_terrier', 'Cairn Terrier'), ('canaan_dog', 'Canaan Dog'), ('italian_corso_dog', 'Italian Corso Dog'), ('bergamasco_shepherd', 'Bergamasco Shepherd'), ('maremma-abruzzes_sheepdog', 'Maremma-Abruzzes Sheepdog'), ('poodle', 'Poodle'), ('portuguese_water_dog', 'Portuguese Water Dog'), ('castro_laboreiro_dog', 'Castro Laboreiro Dog'), ('saint_miguel_cattle_dog', 'Saint Miguel Cattle Dog'), ('portuguese_sheepdog', 'Portuguese Sheepdog'), ('estrela_mountain_dog', 'Estrela Mountain Dog'), ('cavalier_king_charles_spaniel', 'Cavalier King Charles Spaniel'), ('czechoslovakian_wolfdog', 'Czechoslovakian Wolfdog'), ('bohemian_wirehaired_pointing_griffon', 'Bohemian Wirehaired Pointing Griffon'), ('cesky_terrier', 'Cesky Terrier'), ('polish_greyhound', 'Polish Greyhound'), ('chesapeake_bay_retriever', 'Chesapeake Bay Retriever'), ('artois_hound', 'Artois Hound'), ('belgian_shepherd_dog', 'Belgian Shepherd Dog'), ('pyrenean_sheepdog)_smooth-faced', 'Pyrenean Sheepdog, Smooth-faced'), ('pyrenean_sheepdog)_longhaired', 'Pyrenean Sheepdog, Longhaired'), ('pyrenean_mountain_dog', 'Pyrenean Mountain Dog'), ('bloodhound', 'Bloodhound'), ('chihuahua', 'Chihuahua'), ('japanese_chin', 'Japanese Chin'), ('chinese_crested_dog', 'Chinese Crested Dog'), ('chow_chow', 'Chow Chow'), ('uruguayan_cimarron', 'Uruguayan Cimarron'), ('southeastern_european_shepherd', 'Southeastern European Shepherd'), ('romanian_carpathian_shepherd_dog', 'Romanian Carpathian Shepherd Dog'), ('romanian_mioritic_shepherd_dog', 'Romanian Mioritic Shepherd Dog'), ("cirneco_dell'etna", "Cirneco dell'Etna"), ('clumber_spaniel', 'Clumber Spaniel'), ('anatolian_shepherd_dog', 'Anatolian Shepherd Dog'), ('collie)_rough', 'Collie, Rough'), ('collie)_smooth', 'Collie, Smooth'), ('coton_de_tulear', 'Coton de Tulear'), ('montenegrin_mountain_hound', 'Montenegrin Mountain Hound'), ('curly_coated_retriever', 'Curly Coated Retriever'), ('dachshund', 'Dachshund'), ('dalmatian', 'Dalmatian'), ('dandie_dinmont_terrier', 'Dandie Dinmont Terrier'), ('danish-swedish_farmdog', 'Danish-Swedish Farmdog'), ('deerhound', 'Deerhound'), ('german_wirehaired_pointer', 'German Wirehaired Pointer'), ('german_shorthaired_pointer', 'German Shorthaired Pointer'), ('german_longhaired_pointer', 'German Longhaired Pointer'), ('german_rough-haired_pointer', 'German Rough-haired Pointer'), ('german_hound', 'German Hound'), ('great_dane', 'Great Dane'), ('boxer', 'Boxer'), ('german_hunting_terrier', 'German Hunting Terrier'), ('german_pinscher', 'German Pinscher'), ('german_shepherd_dog', 'German Shepherd Dog'), ('german_spitz', 'German Spitz'), ('german_spaniel', 'German Spaniel'), ('tibetan_mastiff', 'Tibetan Mastiff'), ('dobermann', 'Dobermann'), ('dogo_argentino', 'Dogo Argentino'), ('dogo_canario', 'Dogo Canario'), ('dogue_de_bordeaux', 'Dogue de Bordeaux'), ('drentsche_partridge_dog', 'Drentsche Partridge Dog'), ('drever', 'Drever'), ('hungarian_wirehaired_pointer', 'Hungarian Wirehaired Pointer'), ('norwegian_hound', 'Norwegian Hound'), ('english_cocker_spaniel', 'English Cocker Spaniel'), ('english_foxhound', 'English Foxhound'), ('english_pointer', 'English Pointer'), ('english_setter', 'English Setter'), ('english_springer_spaniel', 'English Springer Spaniel'), ('english_toy_terrier_(english_black-and-tan_terrier)', 'English Toy Terrier (English Black-and-Tan Terrier)'), ('entlebuch_cattle_dog', 'Entlebuch Cattle Dog'), ('blue_picardy_spaniel', 'Blue Picardy Spaniel'), ('brittany_spaniel', 'Brittany Spaniel'), ('french_spaniel', 'French Spaniel'), ('continental_toy_spaniel', 'Continental Toy Spaniel'), ('picardy_spaniel', 'Picardy Spaniel'), ('pont-audemer_spaniel', 'Pont-Audemer Spaniel'), ('transylvanian_hound', 'Transylvanian Hound'), ('eurasian', 'Eurasian'), ('field_spaniel', 'Field Spaniel'), ('fila_brasileiro', 'Fila Brasileiro'), ('flat_coated_retriever', 'Flat Coated Retriever'), ('fox_terrier)_smooth', 'Fox Terrier, Smooth'), ('fox_terrier)_wire', 'Fox Terrier, Wire'), ('french_white-and-black_hound', 'French White-and-Black Hound'), ('french_white-and-orange_hound', 'French White-and-Orange Hound'), ('french_tricolour_hound', 'French Tricolour Hound'), ('spanish_greyhound', 'Spanish Greyhound'), ('old_danish_pointer', 'Old Danish Pointer'), ('gascon_saintongeois', 'Gascon Saintongeois'), ('golden_retriever', 'Golden Retriever'), ('polish_hunting_dog', 'Polish Hunting Dog'), ('gordon_setter', 'Gordon Setter'), ('catalan_sheepdog', 'Catalan Sheepdog'), ('great_anglo-french_white-and-black_hound', 'Great Anglo-French White-and-Black Hound'), ('great_anglo-french_white-and-orange_hound', 'Great Anglo-French White-and-Orange Hound'), ('great_anglo-french_tricolour_hound', 'Great Anglo-French Tricolour Hound'), ('grand_basset_griffon_vendeen', 'Grand Basset Griffon Vendeen'), ('great_gascony_blue', 'Great Gascony Blue'), ('grand_griffon_vendeen', 'Grand Griffon Vendeen'), ('greyhound', 'Greyhound'), ('wirehaired_pointing_griffon_korthals', 'Wirehaired Pointing Griffon Korthals'), ('griffon_belge', 'Griffon Belge'), ('blue_gascony_griffon', 'Blue Gascony Griffon'), ('griffon_bruxellois', 'Griffon Bruxellois'), ('fawn_brittany_griffon', 'Fawn Brittany Griffon'), ('griffon_nivernais', 'Griffon Nivernais'), ('greenland_dog', 'Greenland Dog'), ('large_munsterlander', 'Large Munsterlander'), ('great_swiss_mountain_dog', 'Great Swiss Mountain Dog'), ('halden_hound', 'Halden Hound'), ('hamiltonstovare', 'Hamiltonstovare'), ('hanoverian_scenthound', 'Hanoverian Scenthound'), ('harrier', 'Harrier'), ('hellenic_hound', 'Hellenic Hound'), ('hokkaido', 'Hokkaido'), ('dutch_shepherd_dog', 'Dutch Shepherd Dog'), ('dutch_smoushond', 'Dutch Smoushond'), ('hovawart', 'Hovawart'), ('croatian_shepherd_dog', 'Croatian Shepherd Dog'), ('hygen_hound', 'Hygen Hound'), ('south_russian_shepherd_dog', 'South Russian Shepherd Dog'), ('irish_glen_of_imaal_terrier', 'Irish Glen of Imaal Terrier'), ('irish_red_setter', 'Irish Red Setter'), ('irish_red_and_white_setter', 'Irish Red and White Setter'), ('irish_soft_coated_wheaten_terrier', 'Irish Soft Coated Wheaten Terrier'), ('irish_terrier', 'Irish Terrier'), ('irish_water_spaniel', 'Irish Water Spaniel'), ('irish_wolfhound', 'Irish Wolfhound'), ('icelandic_sheepdog', 'Icelandic Sheepdog'), ('istrian_shorthaired_scenthound', 'Istrian Shorthaired Scenthound'), ('istrian_wirehaired_scenthound', 'Istrian Wirehaired Scenthound'), ('jack_russell_terrier', 'Jack Russell Terrier'), ('jamthund', 'Jamthund'), ('yugoslavian_shepherd_dog_(sharplanina)', 'Yugoslavian Shepherd Dog (Sharplanina)'), ('kai', 'Kai'), ('karelian_bear_dog', 'Karelian Bear Dog'), ('caucasian_shepherd_dog', 'Caucasian Shepherd Dog'), ('kerry_blue_terrier', 'Kerry Blue Terrier'), ('king_charles_spaniel', 'King Charles Spaniel'), ('kishu', 'Kishu'), ('small_munsterlander', 'Small Munsterlander'), ('komondor', 'Komondor'), ('korea_jindo_dog', 'Korea Jindo Dog'), ('karst_shepherd_dog', 'Karst Shepherd Dog'), ('kromfohrlander', 'Kromfohrlander'), ('kuvasz', 'Kuvasz'), ('labrador_retriever', 'Labrador Retriever'), ('romagna_water_dog', 'Romagna Water Dog'), ('lakeland_terrier', 'Lakeland Terrier'), ('lancashire_heeler', 'Lancashire Heeler'), ('landseer)', 'Landseer,'), ('lapponian_herder', 'Lapponian Herder'), ('leonberger', 'Leonberger'), ('lhasa_apso', 'Lhasa Apso'), ('hungarian_greyhound', 'Hungarian Greyhound'), ('maltese', 'Maltese'), ('manchester_terrier', 'Manchester Terrier'), ('mastiff', 'Mastiff'), ('spanish_mastiff', 'Spanish Mastiff'), ('pyrenean_mastiff', 'Pyrenean Mastiff'), ('neapolitan_mastiff', 'Neapolitan Mastiff'), ('miniature_bull_terrier', 'Miniature Bull Terrier'), ('mudi', 'Mudi'), ('kooikerhondje', 'Kooikerhondje'), ('dutch_schapendoes', 'Dutch Schapendoes'), ('newfoundland', 'Newfoundland'), ('japanese_spitz', 'Japanese Spitz'), ('japanese_terrier', 'Japanese Terrier'), ('norfolk_terrier', 'Norfolk Terrier'), ('norrbottenspitz', 'Norrbottenspitz'), ('norwegian_buhund', 'Norwegian Buhund'), ('norwegian_elkhound_grey', 'Norwegian Elkhound Grey'), ('norwegian_elkhound_black', 'Norwegian Elkhound Black'), ('norwegian_lundehund', 'Norwegian Lundehund'), ('norwich_terrier', 'Norwich Terrier'), ('nova_scotia_duck_tolling_retriever', 'Nova Scotia Duck Tolling Retriever'), ('polish_hound', 'Polish Hound'), ('old_english_sheepdog_(bobtail)', 'Old English Sheepdog (Bobtail)'), ('austrian_pinscher', 'Austrian Pinscher'), ('otterhound', 'Otterhound'), ('parson_russell_terrier', 'Parson Russell Terrier'), ('pekingese', 'Pekingese'), ('burgos_pointer', 'Burgos Pointer'), ('portuguese_pointer', 'Portuguese Pointer'), ('spanish_water_dog', 'Spanish Water Dog'), ('peruvian_hairless_dog', 'Peruvian Hairless Dog'), ('petit_basset_griffon_vendeen', 'Petit Basset Griffon Vendeen'), ('small_gascony_blue', 'Small Gascony Blue'), ('petit_brabançon', 'Petit Brabançon'), ('little_lion_dog', 'Little Lion Dog'), ('pharaoh_hound', 'Pharaoh Hound'), ('italian_greyhound', 'Italian Greyhound'), ('canarian_warren_hound_(canarian_podenco)', 'Canarian Warren Hound (Canarian Podenco)'), ('ibizan_hound', 'Ibizan Hound'), ('portuguese_warren_hound_(portuguese_podengo)', 'Portuguese Warren Hound (Portuguese Podengo)'), ('poitevin', 'Poitevin'), ('polish_lowland_sheepdog', 'Polish Lowland Sheepdog'), ('tatra_shepherd_dog', 'Tatra Shepherd Dog'), ('porcelaine', 'Porcelaine'), ('save_valley_scenthound', 'Save Valley Scenthound'), ('pudelpointer', 'Pudelpointer'), ('pug', 'Pug'), ('puli', 'Puli'), ('pumi', 'Pumi'), ('rafeiro_of_alentejo', 'Rafeiro of Alentejo'), ('rhodesian_ridgeback', 'Rhodesian Ridgeback'), ('giant_schnauzer', 'Giant Schnauzer'), ('rottweiler', 'Rottweiler'), ('hungarian_shorthaired_pointer', 'Hungarian Shorthaired Pointer'), ('russian_hunting_sighthound_(borzoi)', 'Russian Hunting Sighthound (Borzoi)'), ('russian_black_terrier', 'Russian Black Terrier'), ('russian_toy', 'Russian Toy'), ('russian-european_laika', 'Russian-European Laika'), ('saarloos_wolfdog', 'Saarloos Wolfdog'), ('spanish_hound', 'Spanish Hound'), ('saint_bernard', 'Saint Bernard'), ('saluki', 'Saluki'), ('samoyed', 'Samoyed'), ('schillerstovare', 'Schillerstovare'), ('schipperke', 'Schipperke'), ('schnauzer', 'Schnauzer'), ('swiss_hound', 'Swiss Hound'), ('small_swiss_hound', 'Small Swiss Hound'), ('scottish_terrier', 'Scottish Terrier'), ('sealyham_terrier', 'Sealyham Terrier'), ('italian_hound)_rough-haired', 'Italian Hound, Rough-haired'), ('italian_hound)_shorthaired', 'Italian Hound, Shorthaired'), ('shar_pei', 'Shar Pei'), ('shetland_sheepdog', 'Shetland Sheepdog'), ('shiba', 'Shiba'), ('shih_tzu', 'Shih Tzu'), ('shikoku', 'Shikoku'), ('siberian_husky', 'Siberian Husky'), ('skye_terrier', 'Skye Terrier'), ('arabian_greyhound', 'Arabian Greyhound'), ('slovakian_chuvach', 'Slovakian Chuvach'), ('wirehaired_slovakian_pointer', 'Wirehaired Slovakian Pointer'), ('slovakian_hound', 'Slovakian Hound'), ('smalandsstovare', 'Smalandsstovare'), ('spinone', 'Spinone'), ('central_asia_shepherd_dog', 'Central Asia Shepherd Dog'), ('serbian_hound', 'Serbian Hound'), ('serbian_tricolour_hound', 'Serbian Tricolour Hound'), ('frisian_pointer', 'Frisian Pointer'), ('staffordshire_bull_terrier', 'Staffordshire Bull Terrier'), ('styrian_coarsehaired_hound', 'Styrian Coarsehaired Hound'), ('finnish_hound', 'Finnish Hound'), ('finnish_lapphund', 'Finnish Lapphund'), ('finnish_spitz', 'Finnish Spitz'), ('sussex_spaniel', 'Sussex Spaniel'), ('swedish_lapphund', 'Swedish Lapphund'), ('taiwan_dog', 'Taiwan Dog'), ('brazilian_terrier', 'Brazilian Terrier'), ('thai_bangkaew_dog', 'Thai Bangkaew Dog'), ('thai_ridgeback_dog', 'Thai Ridgeback Dog'), ('tibetan_spaniel', 'Tibetan Spaniel'), ('tibetan_terrier', 'Tibetan Terrier'), ('tyrolean_hound', 'Tyrolean Hound'), ('bosnian_and_herzegovinian-croatian_shepherd_dog', 'Bosnian and Herzegovinian-Croatian Shepherd Dog'), ('tosa', 'Tosa'), ('swedish_vallhund', 'Swedish Vallhund'), ('italian_volpino', 'Italian Volpino'), ('east_siberian_laika', 'East Siberian Laika'), ('weimaraner', 'Weimaraner'), ('welsh_corgi_cardigan', 'Welsh Corgi Cardigan'), ('welsh_corgi_pembroke', 'Welsh Corgi Pembroke'), ('welsh_springer_spaniel', 'Welsh Springer Spaniel'), ('welsh_terrier', 'Welsh Terrier'), ('west_highland_white_terrier', 'West Highland White Terrier'), ('westphalian_dachsbracke', 'Westphalian Dachsbracke'), ('frisian_water_dog', 'Frisian Water Dog'), ('whippet', 'Whippet'), ('xoloitzcuintle', 'Xoloitzcuintle'), ('yorkshire_terrier', 'Yorkshire Terrier'), ('west_siberian_laika', 'West Siberian Laika'), ('miniature_pinscher', 'Miniature Pinscher'), ('miniature_schnauzer', 'Miniature Schnauzer')], max_length=255, null=True),
        ),
    ]