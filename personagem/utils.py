
def get_personagem_upload_path(instance, filename):
    return 'usuarios/{user_id}/personagens/{personagem_id}/{filename}'.format(personagem_id=instance.id,
                                                                             user_id=instance.usuario.user.id,
                                                                             filename=filename)
