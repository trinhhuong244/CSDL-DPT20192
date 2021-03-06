# Generated by Django 3.0.6 on 2020-06-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_lostdog', '0004_auto_20200609_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_addpost',
            name='accessory',
            field=models.CharField(choices=[('Không', 'Không'), ('Vòng cổ', 'Vòng cổ'), ('Xích', 'Xích'), ('Rọ mõm', 'Rọ mõm')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_addpost',
            name='color',
            field=models.CharField(choices=[('Đen', 'Đen'), ('Nâu', 'Nâu'), ('Vàng', 'Vàng'), ('Đỏ', 'Đỏ'), ('Trắng', 'Trắng'), ('Cam', 'Cam')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_addpost',
            name='location',
            field=models.CharField(choices=[('Thanh Xuân', 'Thanh Xuân'), ('Hai Bà Trưng', 'Hai Bà Trưng'), ('Cầu Giấy', 'Cầu Giấy'), ('Ba Đình', 'Ba Đình'), ('Tây Hồ', 'Tây Hồ')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_addpost',
            name='species',
            field=models.CharField(choices=[('affenpinscher', 'affenpinscher'), ('Afghan_hound', 'Afghan_hound'), ('African_hunting_dog', 'African_hunting_dog'), ('Airedale', 'Airedale'), ('American_Staffordshire_terrier', 'American_Staffordshire_terrier'), ('Appenzeller', 'Appenzeller'), ('Australian_terrier', 'Australian_terrier'), ('basenji', 'basenji'), ('basset', 'basset'), ('beagle', 'beagle'), ('Bedlington_terrier', 'Bedlington_terrier'), ('Bernese_mountain_dog', 'Bernese_mountain_dog'), ('black-and-tan_coonhound', 'black-and-tan_coonhound'), ('Blenheim_spaniel', 'Blenheim_spaniel'), ('bloodhound', 'bloodhound'), ('bluetick', 'bluetick'), ('Border_collie', 'Border_collie'), ('Border_terrier', 'Border_terrier'), ('borzoi', 'borzoi'), ('Boston_bull', 'Boston_bull'), ('Bouvier_des_Flandres', 'Bouvier_des_Flandres'), ('boxer', 'boxer'), ('Brabancon_griffon', 'Brabancon_griffon'), ('briard', 'briard'), ('Brittany_spaniel', 'Brittany_spaniel'), ('bull_mastiff', 'bull_mastiff'), ('cairn', 'cairn'), ('Cardigan', 'Cardigan'), ('Chesapeake_Bay_retriever', 'Chesapeake_Bay_retriever'), ('Chihuahua', 'Chihuahua'), ('chow', 'chow'), ('clumber', 'clumber'), ('cocker_spaniel', 'cocker_spaniel'), ('collie', 'collie'), ('curly-coated_retriever', 'curly-coated_retriever'), ('Dandie_Dinmont', 'Dandie_Dinmont'), ('dhole', 'dhole'), ('dingo', 'dingo'), ('Doberman', 'Doberman'), ('English_foxhound', 'English_foxhound'), ('English_setter', 'English_setter'), ('English_springer', 'English_springer'), ('EntleBucher', 'EntleBucher'), ('Eskimo_dog', 'Eskimo_dog'), ('flat-coated_retriever', 'flat-coated_retriever'), ('French_bulldog', 'French_bulldog'), ('German_shepherd', 'German_shepherd'), ('German_short-haired_pointer', 'German_short-haired_pointer'), ('giant_schnauzer', 'giant_schnauzer'), ('golden_retriever', 'golden_retriever'), ('Gordon_setter', 'Gordon_setter'), ('Great_Dane', 'Great_Dane'), ('Great_Pyrenees', 'Great_Pyrenees'), ('Greater_Swiss_Mountain_dog', 'Greater_Swiss_Mountain_dog'), ('groenendael', 'groenendael'), ('Ibizan_hound', 'Ibizan_hound'), ('Irish_setter', 'Irish_setter'), ('Irish_terrier', 'Irish_terrier'), ('Irish_water_spaniel', 'Irish_water_spaniel'), ('Irish_wolfhound', 'Irish_wolfhound'), ('Italian_greyhound', 'Italian_greyhound'), ('Japanese_spaniel', 'Japanese_spaniel'), ('keeshond', 'keeshond'), ('kelpie', 'kelpie'), ('Kerry_blue_terrier', 'Kerry_blue_terrier'), ('komondor', 'komondor'), ('kuvasz', 'kuvasz'), ('Labrador_retriever', 'Labrador_retriever'), ('Lakeland_terrier', 'Lakeland_terrier'), ('Leonberg', 'Leonberg'), ('Lhasa', 'Lhasa'), ('malamute', 'malamute'), ('malinois', 'malinois'), ('Maltese_dog', 'Maltese_dog'), ('Mexican_hairless', 'Mexican_hairless'), ('miniature_pinscher', 'miniature_pinscher'), ('miniature_poodle', 'miniature_poodle'), ('miniature_schnauzer', 'miniature_schnauzer'), ('Newfoundland', 'Newfoundland'), ('Norfolk_terrier', 'Norfolk_terrier'), ('Norwegian_elkhound', 'Norwegian_elkhound'), ('Norwich_terrier', 'Norwich_terrier'), ('Old_English_sheepdog', 'Old_English_sheepdog'), ('otterhound', 'otterhound'), ('papillon', 'papillon'), ('Pekinese', 'Pekinese'), ('Pembroke', 'Pembroke'), ('Pomeranian', 'Pomeranian'), ('pug', 'pug'), ('redbone', 'redbone'), ('Rhodesian_ridgeback', 'Rhodesian_ridgeback'), ('Rottweiler', 'Rottweiler'), ('Saint_Bernard', 'Saint_Bernard'), ('Saluki', 'Saluki'), ('Samoyed', 'Samoyed'), ('schipperke', 'schipperke'), ('Scotch_terrier', 'Scotch_terrier'), ('Scottish_deerhound', 'Scottish_deerhound'), ('Sealyham_terrier', 'Sealyham_terrier'), ('Shetland_sheepdog', 'Shetland_sheepdog'), ('Shih-Tzu', 'Shih-Tzu'), ('Siberian_husky', 'Siberian_husky'), ('silky_terrier', 'silky_terrier'), ('soft-coated_wheaten_terrier', 'soft-coated_wheaten_terrier'), ('Staffordshire_bullterrier', 'Staffordshire_bullterrier'), ('standard_poodle', 'standard_poodle'), ('standard_schnauzer', 'standard_schnauzer'), ('Sussex_spaniel', 'Sussex_spaniel'), ('Tibetan_mastiff', 'Tibetan_mastiff'), ('Tibetan_terrier', 'Tibetan_terrier'), ('toy_poodle', 'toy_poodle'), ('toy_terrier', 'toy_terrier'), ('vizsla', 'vizsla'), ('Walker_hound', 'Walker_hound'), ('Weimaraner', 'Weimaraner'), ('Welsh_springer_spaniel', 'Welsh_springer_spaniel'), ('West_Highland_white_terrier', 'West_Highland_white_terrier'), ('whippet', 'whippet'), ('wire-haired_fox_terrier', 'wire-haired_fox_terrier'), ('Yorkshire_terrier', 'Yorkshire_terrier')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_addpost',
            name='status',
            field=models.CharField(choices=[('Khoẻ mạnh', 'Khoẻ mạnh'), ('Bị ốm', 'Bị ốm')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_addpost',
            name='time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='image_searchpost',
            name='accessory',
            field=models.CharField(choices=[('Không', 'Không'), ('Vòng cổ', 'Vòng cổ'), ('Xích', 'Xích'), ('Rọ mõm', 'Rọ mõm')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_searchpost',
            name='color',
            field=models.CharField(choices=[('Đen', 'Đen'), ('Nâu', 'Nâu'), ('Vàng', 'Vàng'), ('Đỏ', 'Đỏ'), ('Trắng', 'Trắng'), ('Cam', 'Cam')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_searchpost',
            name='location',
            field=models.CharField(choices=[('Thanh Xuân', 'Thanh Xuân'), ('Hai Bà Trưng', 'Hai Bà Trưng'), ('Cầu Giấy', 'Cầu Giấy'), ('Ba Đình', 'Ba Đình'), ('Tây Hồ', 'Tây Hồ')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_searchpost',
            name='species',
            field=models.CharField(choices=[('affenpinscher', 'affenpinscher'), ('Afghan_hound', 'Afghan_hound'), ('African_hunting_dog', 'African_hunting_dog'), ('Airedale', 'Airedale'), ('American_Staffordshire_terrier', 'American_Staffordshire_terrier'), ('Appenzeller', 'Appenzeller'), ('Australian_terrier', 'Australian_terrier'), ('basenji', 'basenji'), ('basset', 'basset'), ('beagle', 'beagle'), ('Bedlington_terrier', 'Bedlington_terrier'), ('Bernese_mountain_dog', 'Bernese_mountain_dog'), ('black-and-tan_coonhound', 'black-and-tan_coonhound'), ('Blenheim_spaniel', 'Blenheim_spaniel'), ('bloodhound', 'bloodhound'), ('bluetick', 'bluetick'), ('Border_collie', 'Border_collie'), ('Border_terrier', 'Border_terrier'), ('borzoi', 'borzoi'), ('Boston_bull', 'Boston_bull'), ('Bouvier_des_Flandres', 'Bouvier_des_Flandres'), ('boxer', 'boxer'), ('Brabancon_griffon', 'Brabancon_griffon'), ('briard', 'briard'), ('Brittany_spaniel', 'Brittany_spaniel'), ('bull_mastiff', 'bull_mastiff'), ('cairn', 'cairn'), ('Cardigan', 'Cardigan'), ('Chesapeake_Bay_retriever', 'Chesapeake_Bay_retriever'), ('Chihuahua', 'Chihuahua'), ('chow', 'chow'), ('clumber', 'clumber'), ('cocker_spaniel', 'cocker_spaniel'), ('collie', 'collie'), ('curly-coated_retriever', 'curly-coated_retriever'), ('Dandie_Dinmont', 'Dandie_Dinmont'), ('dhole', 'dhole'), ('dingo', 'dingo'), ('Doberman', 'Doberman'), ('English_foxhound', 'English_foxhound'), ('English_setter', 'English_setter'), ('English_springer', 'English_springer'), ('EntleBucher', 'EntleBucher'), ('Eskimo_dog', 'Eskimo_dog'), ('flat-coated_retriever', 'flat-coated_retriever'), ('French_bulldog', 'French_bulldog'), ('German_shepherd', 'German_shepherd'), ('German_short-haired_pointer', 'German_short-haired_pointer'), ('giant_schnauzer', 'giant_schnauzer'), ('golden_retriever', 'golden_retriever'), ('Gordon_setter', 'Gordon_setter'), ('Great_Dane', 'Great_Dane'), ('Great_Pyrenees', 'Great_Pyrenees'), ('Greater_Swiss_Mountain_dog', 'Greater_Swiss_Mountain_dog'), ('groenendael', 'groenendael'), ('Ibizan_hound', 'Ibizan_hound'), ('Irish_setter', 'Irish_setter'), ('Irish_terrier', 'Irish_terrier'), ('Irish_water_spaniel', 'Irish_water_spaniel'), ('Irish_wolfhound', 'Irish_wolfhound'), ('Italian_greyhound', 'Italian_greyhound'), ('Japanese_spaniel', 'Japanese_spaniel'), ('keeshond', 'keeshond'), ('kelpie', 'kelpie'), ('Kerry_blue_terrier', 'Kerry_blue_terrier'), ('komondor', 'komondor'), ('kuvasz', 'kuvasz'), ('Labrador_retriever', 'Labrador_retriever'), ('Lakeland_terrier', 'Lakeland_terrier'), ('Leonberg', 'Leonberg'), ('Lhasa', 'Lhasa'), ('malamute', 'malamute'), ('malinois', 'malinois'), ('Maltese_dog', 'Maltese_dog'), ('Mexican_hairless', 'Mexican_hairless'), ('miniature_pinscher', 'miniature_pinscher'), ('miniature_poodle', 'miniature_poodle'), ('miniature_schnauzer', 'miniature_schnauzer'), ('Newfoundland', 'Newfoundland'), ('Norfolk_terrier', 'Norfolk_terrier'), ('Norwegian_elkhound', 'Norwegian_elkhound'), ('Norwich_terrier', 'Norwich_terrier'), ('Old_English_sheepdog', 'Old_English_sheepdog'), ('otterhound', 'otterhound'), ('papillon', 'papillon'), ('Pekinese', 'Pekinese'), ('Pembroke', 'Pembroke'), ('Pomeranian', 'Pomeranian'), ('pug', 'pug'), ('redbone', 'redbone'), ('Rhodesian_ridgeback', 'Rhodesian_ridgeback'), ('Rottweiler', 'Rottweiler'), ('Saint_Bernard', 'Saint_Bernard'), ('Saluki', 'Saluki'), ('Samoyed', 'Samoyed'), ('schipperke', 'schipperke'), ('Scotch_terrier', 'Scotch_terrier'), ('Scottish_deerhound', 'Scottish_deerhound'), ('Sealyham_terrier', 'Sealyham_terrier'), ('Shetland_sheepdog', 'Shetland_sheepdog'), ('Shih-Tzu', 'Shih-Tzu'), ('Siberian_husky', 'Siberian_husky'), ('silky_terrier', 'silky_terrier'), ('soft-coated_wheaten_terrier', 'soft-coated_wheaten_terrier'), ('Staffordshire_bullterrier', 'Staffordshire_bullterrier'), ('standard_poodle', 'standard_poodle'), ('standard_schnauzer', 'standard_schnauzer'), ('Sussex_spaniel', 'Sussex_spaniel'), ('Tibetan_mastiff', 'Tibetan_mastiff'), ('Tibetan_terrier', 'Tibetan_terrier'), ('toy_poodle', 'toy_poodle'), ('toy_terrier', 'toy_terrier'), ('vizsla', 'vizsla'), ('Walker_hound', 'Walker_hound'), ('Weimaraner', 'Weimaraner'), ('Welsh_springer_spaniel', 'Welsh_springer_spaniel'), ('West_Highland_white_terrier', 'West_Highland_white_terrier'), ('whippet', 'whippet'), ('wire-haired_fox_terrier', 'wire-haired_fox_terrier'), ('Yorkshire_terrier', 'Yorkshire_terrier')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_searchpost',
            name='status',
            field=models.CharField(choices=[('Khoẻ mạnh', 'Khoẻ mạnh'), ('Bị ốm', 'Bị ốm')], max_length=100),
        ),
        migrations.AlterField(
            model_name='image_searchpost',
            name='time',
            field=models.DateField(),
        ),
    ]
