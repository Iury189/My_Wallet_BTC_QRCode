import qrcode

# Método para definir algumas configurações do QR Code
imagem = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4
)
# Anexar o código de uma de minhas BTC Adress Wallet ao QR Code
imagem.add_data('bc1qx6dyr4n9nsty56kf7xhqmd4ppw3lj6csgracpr')
imagem.make(fit = True)
# Criando e colorindo o QRCode
qr = imagem.make_image(fill_color = 'white', back_color = '#F7931A')
# Salvando em arquivo
qr.save('MyWalletBTCQRCode.png')
