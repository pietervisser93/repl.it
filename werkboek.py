import socket
import sys
import subprocess

HOST = '' # Alle beschikbare interfaces
PORT = 8888 # Willekeurige poort (denk aan firewall bij Windows Systemen)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
print('> Socket luistert op poort:',PORT)
# Wacht op connecties (blocking)
conn, addr = s.accept()
# Er is een client verbonden met de server
print('> Verbonden met ' + addr[0] + ':' + str(addr[1]))
# De server meldt zich aan de client
conn.sendall(b'WelkomOpMijnServer, vertel me iets, dan zeg ik hetzelfde terug:\n')
# Wacht op input van de client en geef deze ook weer terug (echo service)
data = conn.recv(1024)
data=str(data.decode('ascii')).rstrip() # # Remove \r | \n | \r\n
print('> Client data ontvangen:'+data+'<eindeData>')
conn.sendall(b"jeStuurdeMijDezeData:"+data.encode())
conn.sendall(b'\n')
# Verbreek de verbinding en sluit de socket
conn.close()
s.close()

###
Stappenplan:
Bouw het script als volgt op en test steeds ieder onderdeel voordat je verder gaat!
1. Zorg allereerst dat je vanaf een andere client kan communiceren met de bovenstaande Python-service
(mag in tweetallen). Let hierbij op de firewall en gebruik als client netcat, telnet (niet de windows telnet
client, linux versie kan meestal wel) of putty (in raw mode). Kortom, zorg dat dit script “werkt”.
2. Als de service werkt: Er is geen foutafhandeling opgenomen in het script bij het maken, binden en
luisteren op een poort. Voeg goede foutafhandeling toe aan de server voor deze stappen in het proces
en test ook dat dit werkt. (Je kan dit zelf testen door als PORT een getal op te geven dat al wordt gebruikt
door windows, je krijgt een overzicht met “netstat -an”.)
3. In het script verbreekt de server de verbinding nadat de client iets heeft verzonden. Zorg ervoor dat de
server blijft luisteren en echo-en tenzij de client het woord "stop" zendt, in dat geval mag het script
stoppen. Kortom: er is een loop nodig.
4. Maak het nu mogelijk dat een client een extern commando verstuurt dat op de server wordt uitgevoerd.
Dit is natuurlijk een veiligheidsrisico: als je niet oppast kan een ander je harde schijf formatteren!
Implementeer dit daarom als volgt: Als de client het woord “CALC” verstuurt dan start je de calculatoren
als de client het woord “NOTEPAD” verstuurt start je notepad. Start alle executables asynchroon.
HU | FNT | ICT | TCSB-V2AUT-16 | Werkboek 9
5. Je hebt het aantal commando’s al beperkt, maar bedenk nog een extra beveiligingslaag, zodat niet
iedereen deze commando's kan uitvoeren, waarmee de oplossing nog veiliger wordt. Bepaal zelf hoe je
dit wilt doen.
6. Iedere keer als een programma wordt gestart moet dit worden gelogd in een logfile op de server.
Vermeld telkens een regel met de datum/tijd en het commando dat werd gestart.
7. Optioneel: Volg de communicatie met een packet analyzer zoals whireshark (hoef je niet te laten zien
aan je docent).###
