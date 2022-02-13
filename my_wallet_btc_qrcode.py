import qrcode

# Método para fazer configurações
imagem = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)
# Anexar o código do meu endereço de wallet ao QR Code
imagem.add_data('bc1qx6dyr4n9nsty56kf7xhqmd4ppw3lj6csgracpr')
imagem.make(fit = True)
# Criando e colorindo o QRCode
qr = imagem.make_image(fill_color = 'white', back_color = '#F7931A')
# Salvando em arquivo 
qr.save('MyWalletBTCQRCode.png')
