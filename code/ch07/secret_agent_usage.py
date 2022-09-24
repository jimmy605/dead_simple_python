from secret_agent import SecretAgent

mouse = SecretAgent("Mouse")
armadillo = SecretAgent('Armadillo')
fox = SecretAgent("Fox")

mouse.remember(('42.864025, -72.568511'))

SecretAgent.inform('The goose honks at midnight.')
print(mouse._codeword)

fox.inform('The duck quacks at midnight.')
print(mouse._codeword)

fox.inquire('Testing')