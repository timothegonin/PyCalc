#!/usr/bin/env python3
"""
Point d'entrée principal de la calculatrice
"""

import sys
import os

# Pour les imports relatifs
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui import CalculatorGUI


def main():
    """Fonction principale - lance l'application"""
    print("=" * 50)
    print("🧮 CALCULATRICE i-gore")
    print("=" * 50)
    print("✨ Interface moderne avec CustomTkinter")
    print("🧪 Architecture MVC testée")
    print("⚡ Prêt pour vos calculs !")
    print("-" * 50)
    
    try:
        # Lance l'interface graphique
        app = CalculatorGUI()
        app.run()
        
    except ImportError as e:
        print("❌ ERREUR : Dépendances manquantes")
        print(f"Détails : {e}")
        print("\n🔧 Solution :")
        print("pip install customtkinter")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ ERREUR inattendue : {e}")
        print("\n🐛 Merci de reporter ce bug !")
        sys.exit(1)
    
    finally:
        print("\n👋 Merci d'avoir utilisé la calculatrice i-gore !")


if __name__ == "__main__":
    main()