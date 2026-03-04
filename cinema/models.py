from django.db import models

# Create your models here.


class VideoProduct(models.Model):
    title = models.Charfield(max_length=128)

class OriginalTitle(models.Model):
    title = modelss.Charfield(max_length=128)
    original_title = models.OneToOneField(
        OriginalTitle,
        )

# CREATE TABLE "cinema_originaltitle" (
#     "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
#     "title" varchar(128) NOT NULL
# );


# CREATE TABLE "cinema_videoproduct" (
#     "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
#     "title" varchar(128) NOT NULL,
#     "original_title_id" bigint NOT NULL UNIQUE REFERENCES "cinema_originaltitle"("id")
# );

