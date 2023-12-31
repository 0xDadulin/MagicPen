# Generated by Django 3.2.13 on 2023-03-23 12:08

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hr_helper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UlepszonyTekst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ton', models.CharField(choices=[('optymistyczny', '😊 Optymistyczny'), ('neutralny', '😐 Neutralny'), ('poważny', '🧐 Poważny'), ('wesoły', '😄 Wesoły'), ('inspirujący', '💡 Inspirujący'), ('przyjacielski', '🤗 Przyjacielski'), ('formalny', '👔 Formalny'), ('ironiczny', '🙃 Ironiczny'), ('krytyczny', '🔍 Krytyczny'), ('żartobliwy', '😜 Żartobliwy'), ('nostalgiczny', '🕰️ Nostalgiczny'), ('romantyczny', '💖 Romantyczny'), ('sarkastyczny', '😏 Sarkastyczny')], max_length=255)),
                ('zastosowanie', models.CharField(choices=[('opis_produktu', '📦 Opis produktu'), ('artykul', '📝 Artykuł'), ('recenzja', '🌟 Recenzja'), ('pomysly_na_artykul', '💡 Pomysły na artykuł na bloga'), ('nazwa_dla_firmy', '🏢 Nazwa dla firmy/projektu'), ('pomysly_na_firme', '🚀 Pomysły na firmę'), ('wezwanie_do_dzialania', '✊ Wezwanie do działania'), ('list_motywacyjny', '📄 List motywacyjny'), ('email', '📧 Email'), ('reklama', '📣 Reklama na FB, IG, LinkedIn itp.'), ('pytania_do_wywiadu', '❓ Pytania do wywiadu'), ('opis_oferty_pracy', '🔍 Opis oferty pracy'), ('generator_slow_kluczowych', '🔖 Generator słów kluczowych/tagów'), ('pomysly_na_posty', '📲 Pomysły na posty na social media'), ('opis_profilu', '👤 Opis profilu (bio)'), ('pytania_i_odpowiedzi', '💬 Pytania i odpowiedzi (Q&A)'), ('odpowiedz_na_recenzje', '💼 Odpowiedz na recenzje/wiadomości'), ('seo_meta_tytul', '🔎 SEO meta tytuł'), ('seo_meta_opis', '📈 SEO meta opis'), ('tekst_piosenki', '🎤 Tekst piosenki'), ('zaswiadczenie', '📄 Zaświadczenie/recenzja'), ('yt_opis_kanalu', '📺 YT - opis kanału'), ('yt_opis_filmu', '🎬 YT - opis filmu'), ('yt_pomysly_na_film', '🎥 YT - pomysły na film')], max_length=255)),
                ('tekst', models.TextField()),
                ('ulepszony_tekst', ckeditor.fields.RichTextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('ulubiony', models.BooleanField(default=False)),
                ('tokens', models.IntegerField(blank=True, null=True)),
                ('liczba_slow', models.IntegerField(blank=True, null=True)),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedFile',
        ),
    ]
