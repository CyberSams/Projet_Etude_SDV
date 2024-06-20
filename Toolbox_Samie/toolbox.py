import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from modules.cvelookup import CVELookUp
from modules.dnslookup import DNSLookUp
from modules.portscan import Nmap
from modules.usernamecheck import checkusername
from modules.fakeidentity import generate_fake_identity
from modules.searchsploit import searchsploit
from fpdf import FPDF
import os

class ToolboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Toolbox")

        # Initialize reports list
        self.reports = []

        # Création des widgets
        self.create_widgets()
    
    def create_widgets(self):
        # Titre
        self.title_label = tk.Label(self.root, text="Toolbox", font=("Helvetica", 30, "bold"), fg="#4B0082")
        self.title_label.pack(pady=20)

        # Section Recherche de donnee
        self.recon_label = tk.Label(self.root, text="Recherche de donnée", font=("Arial", 14, "bold"), fg="#3372A6")
        self.recon_label.pack(pady=5)

        self.cve_button = tk.Button(self.root, text="Recherche CVE", command=self.cve_lookup, bg="#4682B4", fg="white")
        self.cve_button.pack(pady=2)

        self.dns_button = tk.Button(self.root, text="Recherche DNS", command=self.dns_lookup, bg="#4682B4", fg="white")
        self.dns_button.pack(pady=2)

        # Section Scan
        self.scan_label = tk.Label(self.root, text="Scan", font=("Arial", 14, "bold"), fg="#B233FF")
        self.scan_label.pack(pady=5)

        self.nmap_button = tk.Button(self.root, text="Scan de Ports avec Nmap", command=self.nmap_scan, bg="#FC33FF", fg="white")
        self.nmap_button.pack(pady=2)

        # Section Exploitation
        self.exploit_label = tk.Label(self.root, text="Exploitation", font=("Arial", 14, "bold"), fg="#3D4A0D")
        self.exploit_label.pack(pady=5)

        self.exploit_button = tk.Button(self.root, text="Recherche d'Exploit", command=self.exploit_search, bg="#607026", fg="white")
        self.exploit_button.pack(pady=2)

        # Section OSINT
        self.osint_label = tk.Label(self.root, text="OSINT", font=("Arial", 14, "bold"), fg="#706A65")
        self.osint_label.pack(pady=5)

        self.username_button = tk.Button(self.root, text="Recherche de Nom d'Utilisateur", command=self.username_check, bg="#706A65", fg="white")
        self.username_button.pack(pady=2)

        self.fakeid_button = tk.Button(self.root, text="Génération Fausse Identité", command=self.generate_fake_identity, bg="#706A65", fg="white")
        self.fakeid_button.pack(pady=2)

        # Section Générateur Rapport PDF
        self.osint_label = tk.Label(self.root, text="Générateur Rapport PDF", font=("Arial", 14, "bold"), fg="#008080")
        self.osint_label.pack(pady=5)

        self.report_button = tk.Button(self.root, text="Générer Rapport PDF", command=self.generate_pdf_report, bg="#008080", fg="white")
        self.report_button.pack(pady=5)

        # Quitter
        self.quit_button = tk.Button(self.root, text="Quitter", command=self.root.quit, bg="#EC1522", fg="white")
        self.quit_button.pack(pady=10)


    # Recherche de CVE
    def cve_lookup(self):
        cve_id = simpledialog.askstring("Recherche CVE", "Entrez un identifiant CVE (ex: CVE-2024-34823) :")
        if cve_id:
            result = CVELookUp(cve_id)
            self.reports.append({'type': 'CVE Lookup', 'content': f'CVE ID: {cve_id}\nResult: {result}'})
            messagebox.showinfo("Résultat CVE", result)


    # Recherche DNS
    def dns_lookup(self):
        domain = simpledialog.askstring("Recherche DNS", "Entrez un nom de domaine :")
        if domain:
            result = DNSLookUp(domain)
            self.reports.append({'type': 'DNS Lookup', 'content': f'Domain: {domain}\nResult: {result}'})


            # Création de la fenêtre pour afficher les résultats
            result_window = tk.Toplevel(self.root)
            result_window.title("Résultat DNS")
            result_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=100, height=30)
            result_text.pack(padx=10, pady=10)
            result_text.insert(tk.END, result)
            result_text.config(state=tk.DISABLED)


    # Scan de Ports avec Nmap
    def nmap_scan(self):
        target = simpledialog.askstring("Scan de Ports avec Nmap", "Entrez un domaine ou une adresse IP :")
        if target:
            result, version = Nmap(target)
            self.reports.append({'type': 'Nmap Scan', 'content': f'Target: {target}\nResult: {result}'})
            messagebox.showinfo("Résultat Nmap", result)


    # Recherche des vulnérabilité et exploitation sur un service
    def exploit_search(self):
        service = simpledialog.askstring("Recherche d'Exploit", "Rechercher des exploits sur un service (ex: github) :")
        if service:
            result = searchsploit(service)
            self.reports.append({'type': 'Exploit Search', 'content': f'Service: {service}\nResult: {result}'})
            messagebox.showinfo("Résultat d'Exploit", result)


    # Recherche de Nom d'Utilisateur
    def username_check(self):
        username = simpledialog.askstring("Recherche de Nom d'Utilisateur", "Entrez un nom d'utilisateur :")
        if username:
            result = checkusername(username)
            self.reports.append({'type': 'Username Check', 'content': f'Username: {username}\nResult: {result}'})


            # Création de la fenêtre pour afficher les résultats
            result_window = tk.Toplevel(self.root)
            result_window.title("Résultat de Nom d'Utilisateur")
            result_text = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, width=100, height=30)
            result_text.pack(padx=10, pady=10)

            
            # Affichage des résultats avec coloration
            for line in result.split('\n'):
                if "[+]" in line:
                    result_text.insert(tk.END, line + '\n', 'found')
                elif "[-]" in line:
                    result_text.insert(tk.END, line + '\n', 'notfound')
                else:
                    result_text.insert(tk.END, line + '\n')
            
            # Définition des tags de couleur
            result_text.tag_config('found', foreground='green')
            result_text.tag_config('notfound', foreground='red')

            result_text.config(state=tk.DISABLED)


    # Génération Fausse Identité
    def generate_fake_identity(self):
        locale = simpledialog.askstring("Génération Fausse Identité", "Entrez la locale (ex: fr) :")
        if locale:
            result = generate_fake_identity(locale)
            self.reports.append({'type': 'Fake Identity Generation', 'content': f'Locale: {locale}\nResult: {result}'})
            messagebox.showinfo("Fausse Identité", result)


    # Générer le rapport PDF
    def generate_pdf_report(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        
        pdf.set_font("Helvetica", 'B', size=14)
        pdf.cell(200, 10, txt="Rapport de la toolbox", ln=True, align='C')
        pdf.set_font("Helvetica", size=12)

        for report in self.reports:
            pdf.multi_cell(0, 10, txt=f"{report['type']}:\n{report['content']}")
            pdf.ln(10)
        
        pdf_output = os.path.join(os.path.expanduser("~"), "Desktop", "rapport_toolbox.pdf")
        pdf.output(pdf_output)
        messagebox.showinfo("Génération de Rapport", f"Rapport PDF généré : {pdf_output}")


if __name__ == "__main__":

    # Lancer l'interface Tkinter
    root = tk.Tk()
    app = ToolboxApp(root)
    root.mainloop()
