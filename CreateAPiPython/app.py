from flask import Flask, jsonify


app = Flask(__name__)

data = [
    {
    'titel': 'Java',
    'description': 'Java ist eine objektorientierte Programmiersprache und eine eingetragene Marke des Unternehmens Sun Microsystems, welches 2010 von Oracle aufgekauft wurde.'
    },
    {
    'titel': 'Javascript',
    'description': 'JavaScript (kurz JS) ist eine Skriptsprache, die ursprünglich 1995 von Netscape für dynamisches HTML in Webbrowsern entwickelt wurde, um Benutzerinteraktionen auszuwerten, Inhalte zu verändern, nachzuladen oder zu generieren und so die Möglichkeiten von HTML und CSS zu erweitern.'
    },
    {
    'titel': 'c',
    'description': 'C ist eine imperative und prozedurale Programmiersprache, die am meisten zur System- und Anwendungsprogrammierung eingesetzt wird.'
    },
    {
    'titel': 'Python',
    'description': 'Python ist eine universelle üblicherweise interpretierte, höhere Programmiersprache. Python wurde mit dem Ziel größter Einfachheit und Übersichtlichkeit entworfen. '
    },
    {
    'titel':'PHP',
    'description': '„PHP: Hypertext Preprocessor“, ursprünglich „Personal Home Page Tools“ ist eine Skriptsprache mit einer an C und Perl angelehnten Syntax, die hauptsächlich zur Erstellung dynamischer Webseiten oder Webanwendungen verwendet wird.'

    },
    {
    'titel':'Scala',
    'description': 'Scala ist eine funktionale und objektorientierte Programmiersprache.'
    },
    {
    'titel': 'HTLM5',
    'description': 'ist die fünfte Fassung der Hypertext Markup Language (engl. für Hypertext-Auszeichnungssprache), einer Computersprache zur Auszeichnung und Vernetzung von Texten und anderen Inhalten elektronischer Dokumente, vorwiegend im World Wide Web.'
    },
    {
    'titel': 'CSS5',
    'description': ''
    },
    {
    'titel': 'Shell',
    'description': 'Die Unix-Shell oder kurz Shell (englisch für Hülle, Schale) bezeichnet die traditionelle Benutzerschnittstelle unter Unix oder unixoiden Computer-Betriebssystemen.'
    },
    {
    'titel': 'Typescript',
    'description': 'TypeScript ist eine von Microsoft entwickelte Programmiersprache, die auf den Vorschlägen zum Javascript basiert.'
    },
    {
    'titel': 'C++',
    'description': 'C++ ist eine von der ISO genormte Programmiersprache. Sie wurde ab 1979 von Bjarne Stroustrup bei AT&T als Erweiterung der Programmiersprache C entwickelt. C++ ermöglicht sowohl die effiziente und maschinennahe Programmierung als auch eine Programmierung auf hohem Abstraktionsniveau. '
    },
    {
    'titel': 'C#',
    'description': 'c# ist eine typsichere, objektorientierte Allzweck-Programmiersprache. Die Sprache ist an sich plattformunabhängig, wurde aber im Rahmen der .NET-Strategie entwickelt, ist auf diese optimiert und meist in deren Kontext zu finden.'
    },
    {
    'titel': 'F#',
    'description': 'F# ist eine typsichere Multi-Paradigmen-Sprache mit starkem Fokus auf funktionale Programmierung für das .NET-Framework.'
    },
    {
    'titel': 'Bash',
    'description': 'Bash (auch BASH oder bash), die Bourne-again shell, ist eine freie Unix-Shell unter GPL.'
    },
    {
    'titel': 'Processing',
    'description': 'Processing ist eine objektorientierte, stark typisierte Programmiersprache mit zugehöriger integrierter Entwicklungsumgebung. Die Programmiersprache ist auf die Einsatzbereiche Grafik, Simulation und Animation spezialisiert.'
    }, 
    {
    'titel': 'Kotlin',
    'description': 'Kotlin ist eine plattformübergreifende, statisch typisierte Programmiersprache, die in Bytecode für die Java Virtual Machine (JVM) übersetzt wird, aber auch in JavaScript-Quellcode oder (mittels LLVM) in Maschinencode umgewandelt werden kann. '
    },



]

@app.route("/")
def dummy_api():
    return jsonify(data)

if __name__ == "__main__":
    app.run()