# Generated by Django 2.0.6 on 2018-06-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('code', models.CharField(blank=True, max_length=32, null=True)),
                ('title', models.CharField(blank=True, choices=[('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Anguilla', 'Anguilla'), ('Antarctica', 'Antarctica'), ('Antigua_and_Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Aruba', 'Aruba'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('Bahamas', 'Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bermuda', 'Bermuda'), ('Bhutan', 'Bhutan'), ('Plurinational_State_of_Bolivia', 'Plurinational State of Bolivia'), ('Bosnia_and_Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei_Darussalam', 'Brunei Darussalam'), ('Bulgaria', 'Bulgaria'), ('Burkina_Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Cape_Verde', 'Cape Verde'), ('Central_African_Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo', 'Congo'), ('Democratic_Republic_of_the_Congo', 'Democratic Republic of the Congo'), ('Costa_Rica', 'Costa Rica'), ('Cote_dIvoire', "Côte d'Ivoire"), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Curacao', 'Curaçao'), ('Cyprus', 'Cyprus'), ('Czech_Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican_Republic', 'Dominican Republic'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El_Salvador', 'El Salvador'), ('Equatorial_Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('French_Guiana', 'French Guiana'), ('French_Polynesia', 'French Polynesia'), ('Gabon', 'Gabon'), ('Gambia', 'Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Gibraltar', 'Gibraltar'), ('Greece', 'Greece'), ('Greenland', 'Greenland'), ('Grenada', 'Grenada'), ('Guadeloupe', 'Guadeloupe'), ('Guam', 'Guam'), ('Guatemala', 'Guatemala'), ('Guernsey', 'Guernsey'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hong_Kong', 'Hong Kong'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Islamic_Republic_of_Iran', 'Islamic Republic of Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Isle_of_Man', 'Isle of Man'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jersey', 'Jersey'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Democratic_Peoples_Republic_of_Korea', "Democratic People's Republic of Korea"), ('Republic_of_Korea', 'Republic of Korea'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Lao_Peoples_Democratic_Republic', "Lao People's Democratic Republic"), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Macao', 'Macao'), ('Macedonia', 'Macedonia'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Martinique', 'Martinique'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mayotte', 'Mayotte'), ('Mexico', 'Mexico'), ('Federated_States_of_Micronesia', 'Federated States of Micronesia'), ('Republic_of_Moldova', 'Republic of Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar', 'Myanmar'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New_Caledonia', 'New Caledonia'), ('New_Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('Niue', 'Niue'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('State_of_Palestine', 'State of Palestine'), ('Panama', 'Panama'), ('Papua_New_Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Pitcairn', 'Pitcairn'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Puerto_Rico', 'Puerto Rico'), ('Qatar', 'Qatar'), ('Reunion', 'Réunion'), ('Romania', 'Romania'), ('Russian_Federation', 'Russian Federation'), ('Rwanda', 'Rwanda'), ('Saint_Barthelemy', 'Saint Barthélemy'), ('Saint_Helena_Ascension_and_Tristan_da_Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Saint_Kitts_and_Nevis', 'Saint Kitts and Nevis'), ('Saint_Lucia', 'Saint Lucia'), ('Saint_Martin_(French_part)', 'Saint Martin (French part)'), ('Saint_Pierre_and_Miquelon', 'Saint Pierre and Miquelon'), ('Saint_Vincent_and_the_Grenadines', 'Saint Vincent and the Grenadines'), ('Samoa', 'Samoa'), ('San_Marino', 'San Marino'), ('Sao_Tome_and_Principe', 'Sao Tome and Principe'), ('Saudi_Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra_Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Sint_Maarten_(Dutch_part)', 'Sint Maarten (Dutch part)'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Somalia', 'Somalia'), ('South_Africa', 'South Africa'), ('South_Sudan', 'South Sudan'), ('Spain', 'Spain'), ('Sri_Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Suriname', 'Suriname'), ('Svalbard_and_Jan_Mayen', 'Svalbard and Jan Mayen'), ('Swaziland', 'Swaziland'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syrian_Arab_Republic', 'Syrian Arab Republic'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('United_Republic_of_Tanzania', 'United Republic of Tanzania'), ('Thailand', 'Thailand'), ('Timor-Leste', 'Timor-Leste'), ('Togo', 'Togo'), ('Tokelau', 'Tokelau'), ('Tonga', 'Tonga'), ('Trinidad_and_Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United_Arab_Emirates', 'United Arab Emirates'), ('United_Kingdom', 'United Kingdom'), ('United_States_Of_America', 'United States of America'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Bolivarian_Republic_of_Venezuela', 'Bolivarian Republic of Venezuela'), ('Viet_Nam', 'Viet Nam'), ('Wallis_and_Futuna', 'Wallis and Futuna'), ('Western_Sahara', 'Western Sahara'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=128, null=True)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'db_table': 'countries',
            },
        ),
    ]
