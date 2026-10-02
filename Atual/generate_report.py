
from pathlib import Path
import csv, json
from datetime import datetime
from db import init_db, latest_snapshots, portfolio_actions, cash_plans

BASE=Path(__file__).resolve().parent
REPORTS=BASE/"reports"

def generate():
    init_db()
    REPORTS.mkdir(exist_ok=True)
    rows=latest_snapshots()
    actions=portfolio_actions(limit=100)
    plans=cash_plans(limit=1)
    stamp=datetime.now().strftime("%Y-%m-%d_%H%M")
    html_path=REPORTS/f"ranking_{stamp}.html"

    plan_html="<p>Sem plano de caixa ainda.</p>"
    if plans:
        p=json.loads(plans[0]["plan_json"])
        trs="".join(
            f"<tr><td>{i['product']}</td><td>{i['action']}</td><td>{i['priority_score']}</td>"
            f"<td>{i['recommended_units']}</td><td>R$ {i['capital_allocated']:.2f}</td>"
            f"<td>R$ {i['expected_lot_profit']:.2f}</td></tr>"
            for i in p["items"]
        )
        plan_html=f"""
        <p>Caixa: R$ {p['budget']:.2f} | Reserva: R$ {p['reserve_value']:.2f} |
        Alocado: R$ {p['allocated']:.2f} | Sobra: R$ {p['cash_remaining']:.2f}</p>
        <table><tr><th>Produto</th><th>Ação</th><th>Prioridade</th><th>Comprar</th><th>Capital</th><th>Lucro esperado</th></tr>{trs}</table>
        """

    html=f"""<!doctype html><meta charset='utf-8'><title>Garimpeiro V7</title>
    <style>body{{font-family:Arial;max-width:1250px;margin:30px auto;padding:0 20px}}
    table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid #ddd;padding:8px}}
    th{{background:#f3f3f3}}</style>
    <h1>Garimpeiro Shopee V7 — Caixa & Estoque</h1>
    <p>Gerado em {datetime.now().strftime("%d/%m/%Y %H:%M")}</p>
    <h2>Plano de compra</h2>{plan_html}
    """
    html_path.write_text(html,encoding="utf-8")
    return html_path

if __name__=="__main__":
    print(generate())
