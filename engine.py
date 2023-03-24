import face_recognition as fr


def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if (len(rostos) > 0):
        return True, rostos

    return False, []


def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    Matheus = reconhece_face("./img/eu.jpg")
    if (Matheus[0]):
        rostos_conhecidos.append(Matheus[1][0])
        nomes_dos_rostos.append("Matheus")

    Romário = reconhece_face("./img/romario.jpg")
    if (Romário[0]):
        rostos_conhecidos.append(Romário[1][0])
        nomes_dos_rostos.append("Romário")

    return rostos_conhecidos, nomes_dos_rostos