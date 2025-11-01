from models import Lead
from stages import DEFAULT_STAGE
from repo import LeadRepository


lead_backend = LeadRepository()

def add_lead():
    name = input("Name: ")
    company = input("Empresa: ")
    email = input("E-mail: ")

    lead = Lead(name, company, email, DEFAULT_STAGE)
    modeled_lead = lead.struct_lead() # model_lead() é o struct_lead
    lead_backend.create_lead(modeled_lead)
    print("Lead adicionado")

def list_leads():
    leads = lead_backend.read_leads()
    if not leads:
        print("Nenhum lead ainda")
        return

    print(f"\n## | {"Nome":<20} | {"Empresa":<20} | {"E-mail":<20}")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<20} | {lead["company"]:<20} | {lead["email"]:<20}")

def search_leads():
    user_search = input("Buscar por: ").strip().lower()

    if not user_search:
        print("Consulta vazia")
        return

    leads = lead_backend.read_leads() # ler todos os meus leads do arquivo leads.json
    results = []

    for i, lead in enumerate(leads):
        lead_str = f"{lead["name"]} {lead["company"]} {lead["email"]}".lower()

        if user_search in lead_str:
            results.append(lead)

    if not results:
        print("Nada encontrado")
        return

    print(f"\n## | {"Nome":<20} | {"Empresa":<20} | {"E-mail":<20}")
    for i, lead in enumerate(results):
        print(f"{i:02d} | {lead["name"]:<20} | {lead["company"]:<20} | {lead["email"]:<20}")

def export_leads():
    path_csv = lead_backend.csv_export()
    if path_csv is None:
        print("Erro... Feche o arquivo se estiver aberto e tente novamente !")
    else:
        print(f"Arquivo CSV exportado com sucesso para {path_csv}")

def main():
    while True:
        print_menu()
        op = input("Escolha: ")

        if op == "1":
            print("Lead adicionado")
            add_lead()
        elif op == "2":
            print("Listar leads")
            list_leads()
        elif op == "3":
            search_leads()
        elif op == "4":
            export_leads()
        elif op == "0":
            print("Até mais")
            break
        else:
            print("Opção inválida")

def print_menu():
    print("\nMini CRM de Leads - (Adicionar/Listar)")
    print("[1] Adicionar Leads")
    print("[2] Listar Leads")
    print("[3] Buscar leads (nome/empresa/e-mail)")
    print("[4] Exportar leads com csv")


    print("[0] Sair")

# main()
if __name__ == "__main__":
    main()