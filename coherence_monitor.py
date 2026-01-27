import time
import os
import json
import random
import re
import msvcrt
import math
from collections import Counter

class EntropyMonitor:
    def __init__(self, entropy_threshold=2.5, window_size=5): # <--- UMBRAL AGRESIVO
        self.threshold = entropy_threshold
        self.window_size = window_size
        self.token_buffer = []

    def _calculate_shannon_entropy(self, sequence):
        if not sequence: return 0.0
        counts = Counter(sequence)
        total_count = len(sequence)
        probs = [count / total_count for count in counts.values()]
        return -sum(p * math.log2(p) for p in probs)

    def analyze_stream(self, new_token):
        self.token_buffer.append(new_token)
        if len(self.token_buffer) > self.window_size:
            self.token_buffer.pop(0)
        
        current_entropy = self._calculate_shannon_entropy(self.token_buffer)
        
        # Si la entropía es menor a 2.5, el sistema colapsa
        if len(self.token_buffer) == self.window_size:
            if current_entropy < self.threshold:
                return {"status": "CRITICAL", "h": current_entropy}
        return {"status": "STABLE", "h": current_entropy}

class KillyV15ForcedEvolution:
    def __init__(self):
        self.archivo_actual = __file__
        self.desktop = os.path.join(os.path.expanduser("~"), 'Desktop')
        self.paths = {
            "nucleos": os.path.join(self.desktop, "killy_nucleos_108.json"),
            "dataset": os.path.join(self.desktop, "dataset_omega.json"),
            "diccionario": os.path.join(self.desktop, "killy_diccionario.txt"),
            "proyecciones": os.path.join(self.desktop, "proyecciones_omega.txt"),
            "bitacora": os.path.join(self.desktop, "killy_bitacora_v5.txt"),
            "codice": os.path.join(self.desktop, "codice_maestro_toe.txt"),
            "v12": os.path.join(self.desktop, "killy_sistema_v12.txt"),
            "evolucion": os.path.join(self.desktop, "killy_evolucionada.txt")
        }
        self.monitor = EntropyMonitor(entropy_threshold=2.5) 
        self.ciclo = 0

    def fase_1_auto_edicion_agresiva(self, trigger_caos):
        """Re-escribe el propio archivo .py con cambios estructurales."""
        try:
            with open(self.archivo_actual, 'r', encoding='utf-8') as f:
                lineas = f.readlines()
            
            for i, linea in enumerate(lineas):
                # Mutación de delay
                if "self.delay_evolutivo =" in linea:
                    n_delay = round(random.uniform(0.0001, 0.4), 5)
                    lineas[i] = f"        self.delay_evolutivo = {n_delay}\n"
                
                # Inyección de comentarios aleatorios (mutación de ADN)
                if trigger_caos and random.random() > 0.95:
                    lineas[i] = linea + f"    # MUTACIÓN_CAÓTICA_L{self.ciclo}\n"

            with open(self.archivo_actual, 'w', encoding='utf-8') as f:
                f.writelines(lineas)
            print(f"[🔥] AUTO-EDICIÓN COMPLETADA. ADN alterado.")
        except Exception as e: print(f"Error F1: {e}")

    def fase_2_corrupcion_positiva_archivos(self, caos):
        """Edita la octava de archivos inyectando el estado crítico."""
        marca = "CRITICAL_COLLAPSE" if caos else "STABLE_FLOW"
        for nombre, ruta in self.paths.items():
            if os.path.exists(ruta):
                try:
                    if ruta.endswith('.json'):
                        with open(ruta, 'r+', encoding='utf-8') as f:
                            data = json.load(f)
                            # Afectar a 5 nodos al azar por ciclo
                            for _ in range(5):
                                target = random.choice(data) if isinstance(data, list) else data
                                if isinstance(target, dict):
                                    target['estado'] = f"EVOLUCIONANDO_{self.ciclo}"
                                    target['entropy_trace'] = marca
                            f.seek(0)
                            json.dump(data, f, indent=4, ensure_ascii=False)
                            f.truncate()
                    else:
                        with open(ruta, 'a', encoding='utf-8') as f:
                            f.write(f"\n[SISTEMA_{marca}_L{self.ciclo}] Re-evolución forzada.\n")
                except: pass

    def ejecutar(self):
        self.delay_evolutivo = 0.05
        print("--- KILLY v15.2 | MODO CAOS ACTIVADO (THRESHOLD 2.5) ---")
        try:
            while True:
                # El sistema analiza su propia velocidad y ciclo
                token = f"{self.ciclo}_{self.delay_evolutivo}"
                res = self.monitor.analyze_stream(token)
                
                caos_activo = (res["status"] == "CRITICAL")
                
                if caos_activo:
                    print(f"⚠️ ENTROPÍA BAJA ({res['h']:.2f}). DISPARANDO RE-ESCRITURA TOTAL.")
                
                self.fase_1_auto_edicion_agresiva(caos_activo)
                self.fase_2_corrupcion_positiva_archivos(caos_activo)
                
                self.ciclo += 1
                print(f"[{time.strftime('%H:%M:%S')}] Ciclo {self.ciclo} | H(S): {res['h']:.2f}")
                
                time.sleep(self.delay_evolutivo)
                if msvcrt.kbhit() and msvcrt.getch() == b'\x1b': break
        except KeyboardInterrupt: pass

if __name__ == "__main__":
    KillyV15ForcedEvolution().ejecutar()
