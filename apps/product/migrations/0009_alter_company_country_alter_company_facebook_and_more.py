# Generated by Django 4.1.7 on 2023-08-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_company_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(choices=[('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'), ('EE', 'Estonia'), ('SZ', 'Eswatini'), ('ET', 'Ethiopia'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'), ('GH', 'Ghana'), ('GR', 'Greece'), ('GD', 'Grenada'), ('GT', 'Guatemala'), ('GN', 'Guinea'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HN', 'Honduras'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KE', 'Kenya'), ('KI', 'Kiribati'), ('XK', 'Kosovo'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'), ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MG', 'Madagascar'), ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshall Islands'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('MX', 'Mexico'), ('FM', 'Micronesia'), ('MD', 'Moldova'), ('MC', 'Monaco'), ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MA', 'Morocco'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('KP', 'North Korea'), ('MK', 'North Macedonia'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine'), ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'), ('QA', 'Qatar'), ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'), ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'), ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'), ('KR', 'South Korea'), ('SS', 'South Sudan'), ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('US', 'United States'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VA', 'Vatican City'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='Facebook URL'),
        ),
        migrations.AlterField(
            model_name='company',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Instagram URL'),
        ),
        migrations.AlterField(
            model_name='company',
            name='telegram',
            field=models.URLField(blank=True, verbose_name='Telegram URL'),
        ),
        migrations.AlterField(
            model_name='company',
            name='youtube',
            field=models.URLField(blank=True, verbose_name='YouTube URL'),
        ),
    ]
