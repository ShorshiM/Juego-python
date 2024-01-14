class Juego(id.Cargar):
    # atributos de la clase Juego
    __nombre_personaje = ""
    __salud_personaje = 100
    __fuerza_personaje = 2
    __daño_personaje = 6
    __espada = 4
    __hacha = 2
    __curacion = 10
    __curacion_personaje = 3  # cuantas curaciones tiene
    __curacion_grande = 22
    __curacion_grande_personaje = 2  # cuantas curaciones tiene
    __vida_enemigo = 100
    __daño_enemigo = 4
    __exp_personaje = 0
    __nivel_personaje = 1
    __game_over = False
    __maximo_curacion_enemigo = 0
    __uso_espada = 0
    __uso_hacha = 0
    __experiencia_maxima = 100
    __nivel_maximo = False
    __validar = 1
    __probabilidad_golpe_critico_personaje = 0
    __probabilidad_golpe_critico_enemigo = 0
    __anillo_inmortal = 0
    __frase_anillo = ""
    __tiene_espada = False
    __tiene_hacha = False

    # constructor de la clase Juego
    def __init__(self) -> None:
        super().__init__()

    # se define los set y get de los atributos
    # pasamos de metodos a propiedades
    @property
    def nombre_personaje(self):
        return self.__nombre_personaje

    @nombre_personaje.setter
    def nombre_personaje(self, nombre_personaje):
        self.__nombre_personaje = nombre_personaje

    # pasamos de metodos a propiedades
    @property
    def game_over(self):
        return self.__game_over

    # metodos de la clase Juego
    def mover(self, movimiento):
        frase_espada = ""
        if self.__uso_espada > 0:
            frase_espada = f" - Usos de espada: {self.__uso_espada}"
        frase_hacha = ""
        if self.__uso_hacha > 0:
            frase_hacha = f" - Usos de hacha: {self.__uso_hacha}"
        # reinicia el atributo para el siguiente movimiento
        self.__enemigo = False
        # dependiendo del movimiento con random hay probabilidad de que encuentre un enemigo
        if movimiento == 1:
            numero = random.randint(1, 6)
            if numero >= 1 or numero <= 3:
                self.__enemigo = True
        elif movimiento == 2:
            numero = random.randint(1, 3)
            if numero == 1 or numero == 2:
                self.__enemigo = True
        elif movimiento == 3:
            numero = random.randint(1, 8)
            if numero >= 3 and numero <= 6:
                self.__enemigo = True
        elif movimiento == 4:
            # opcion 4 ver estadisticas
            print(
                "      ------    Estadisticas del personaje     ------\n"
                + f" - Nombre: {self.__nombre_personaje}      - Vida: {self.__salud_personaje}\n"
                + f" - Fuerza: {self.__fuerza_personaje}      - Daño: {self.__daño_personaje}\n"
                + f" - Experiencia: {self.__exp_personaje}\n"
                + f" - Nivel: {self.__nivel_personaje}"
            )
            # se ponen los dos false para que solo se vea esto en nivel maximo
            print(self.barra_progreso(False, self.__nivel_maximo, False))
            print(
                f" - Curaciones pequeñas: {self.__curacion_personaje}\n"
                + f" - Curaciones grandes: {self.__curacion_grande_personaje}\n"
                + f"{frase_hacha}\n"
                + f"{frase_espada}\n"
                + f"{self.__frase_anillo}"
            )
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
        if movimiento == 5:
            # opcion 5 se acaba el juego
            self.__game_over = True
        elif movimiento != 4 and movimiento != 5:
            self.accion()

    def accion(self):
        # si se encontro un enemigo empieza la batalla
        if self.__enemigo:
            print("Enemigo encontrado")
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
            # usos de las armas se reinicia con cada enemigo
            usos = [int(self.__uso_espada), int(self.__uso_hacha)]
            salud_enemigo = self.__vida_enemigo
            salud_personaje = self.__salud_personaje
            # maximo de veces que se puede curar el enemigo
            maximo_curacion = int(4 + self.__maximo_curacion_enemigo)
            # rondas posibles
            for ronda in range(1, 151):
                # verifica si la salud de cualquiera de los dos es 0
                if salud_enemigo <= 0 or salud_personaje <= 0:
                    # caso para cuando la salud del enemigo es 0
                    if salud_enemigo <= 0:
                        exp_ganada = 97 + random.randint(
                            self.__nivel_personaje, (self.__nivel_personaje * 3)
                        )
                        subir_nivel = False
                        self.__exp_personaje += exp_ganada
                        # verifica si sube de nivel
                        if self.__exp_personaje >= self.__experiencia_maxima:
                            # lo cambia a true para mostrar subir nivel
                            subir_nivel = True
                            if self.__nivel_personaje == 20:
                                # para que ya no suba de nivel
                                self.__nivel_maximo = True
                                subir_nivel = False
                            else:
                                # esto es para cuando se tenga mas exp ganada pero ya subimos de nivel
                                self.__exp_personaje = (
                                    self.__exp_personaje - self.__experiencia_maxima
                                )
                                # si sube de nivel aumentan los atributos de los 2
                                self.__nivel_personaje += 1
                                self.__daño_personaje += 3
                                # si ya tiene espada y hacha se suman los usos
                                if self.__tiene_espada:
                                    self.__uso_espada += 0.5
                                if self.__tiene_hacha:
                                    self.__uso_hacha += 0.5
                                self.__daño_enemigo += 3
                                self.__fuerza_personaje += 3
                                self.__espada += 1
                                self.__hacha += 1
                                self.__maximo_curacion_enemigo += 0.3
                                self.__vida_enemigo += 20
                                self.__salud_personaje += 15
                                self.__curacion_personaje += 1
                                # cada 5 niveles se suma 100 de experiencia necesaria para que suba de nivel
                                if self.__nivel_personaje % 5 == 0:
                                    self.__experiencia_maxima += 100
                                    # esta variable permite que se aplique la reducción de guiones
                                    self.__validar += 1
                                suerte = random.randint(1, 2)
                                frase = ""
                                if suerte == 2:
                                    self.__curacion_grande_personaje += 1
                                    frase = " - Curacion grande"
                                frase += self.probabilidad_objeto()
                        else:
                            # para cuando solo obtiene experiencia
                            self.__curacion_personaje += 1
                            suerte = random.randint(1, 2)
                            frase = ""
                            if suerte == 2:
                                self.__curacion_grande_personaje += 1
                                frase = " - Curacion grande"
                            frase += self.probabilidad_objeto()
                        frase_nivel = self.barra_progreso(
                            subir_nivel, self.__nivel_maximo, True
                        )
                        print(
                            "                  ------   Ganaste la batalla   ------\n"
                            + f"    - Exp ganada: {exp_ganada}\n"
                            + f"      -Exp total: {self.__exp_personaje}"
                        )
                        print(frase_nivel)
                        print(
                            "   El enemigo solto:\n"
                            + " - Curacion pequeña\n"
                            + f"{frase}"
                        )
                        input(
                            "               ------  Presione enter para continuar  ------       "
                        )
                        id.limpiar_pantalla()
                        break
                    else:
                        if self.__anillo_inmortal == 1:
                            print(
                                "       ------ Haz muerto pero posees el anillo de la inmortalidad ------\n"
                                + "        ----- resucitaste pero en el proceso se rompió el anillo! -----"
                            )
                            self.__frase_anillo = (
                                " - Tu anillo de la inmortalidad esta rota, era única"
                            )
                            self.__anillo_inmortal = 2
                            break
                        else:
                            # caso si el personaje tiene vida 0
                            print(
                                "              ------   Estas muerto   ------\n"
                                + "               ----     Game Over      ----"
                            )
                            input(
                                "       ------  Presione enter para continuar  ------       "
                            )
                            id.limpiar_pantalla()
                            self.__game_over = True
                            break
                else:
                    if salud_personaje <= 0:
                        continue
                    # se llama al metodo usar
                    opcion = self.usar(ronda, usos)
                    # acciones del personaje
                    if opcion == 6:
                        # para la opcion huir
                        print("Escapaste de la pelea")
                        input(
                            "       ------  Presione enter para continuar  ------       "
                        )
                        id.limpiar_pantalla()
                        break
                    else:
                        # cambia la salud del enemigo
                        if opcion >= 1 and opcion <= 3:
                            salud_enemigo = self.atacar(
                                opcion, salud_enemigo, salud_personaje, usos
                            )
                        else:
                            # cambia la salud del personaje
                            salud_personaje = self.atacar(
                                opcion, salud_enemigo, salud_personaje, usos
                            )
                    if salud_enemigo <= 0:
                        continue
                    # turno del enemigo es al azar
                    # valida curaciones máximas del enemigo para que no se cure todo el tiempo
                    if maximo_curacion == 0:
                        turno_enemigo = 2
                    else:
                        turno_enemigo = random.randint(1, 25)
                    # para que se haga el mayor daño posible
                    if turno_enemigo >= 1 and turno_enemigo <= 20:
                        # opcion en la que ataca al personaje
                        critico = random.randint(1, 15)
                        # por medio de random el enemigo puede lanzar un golpe critico
                        if critico >= 3 and critico <= 9:
                            # el golpe critico es del 33 por ciento del daño del enemigo
                            self.__probabilidad_golpe_critico_enemigo = int(
                                self.__daño_enemigo * 0.333
                            )
                        else:
                            self.__probabilidad_golpe_critico_enemigo = 0
                        daño = (
                            self.__daño_enemigo
                            + random.randint(
                                (self.__daño_enemigo - 3), self.__daño_enemigo
                            )
                            + self.__probabilidad_golpe_critico_enemigo
                        )
                        salud_personaje -= daño
                        if salud_personaje < 0:
                            salud_personaje = 0
                        if self.__probabilidad_golpe_critico_enemigo == 0:
                            print(
                                f"{self.__nombre_personaje} recibio un daño de {daño}\n"
                                + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                            )
                        else:
                            print(
                                f"¡Golpe Critico! {self.__nombre_personaje} recibio un daño de {daño}\n"
                                + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                            )
                        input(
                            "       ------  Presione enter para continuar  ------       "
                        )
                        id.limpiar_pantalla()
                    elif turno_enemigo >= 21 and turno_enemigo <= 23:
                        # opcion en la que usa curacion
                        curacion = int(
                            self.__curacion
                            + random.randint(1, 4)
                            + (self.__vida_enemigo * 0.15)
                        )
                        maximo_curacion -= 1
                        # si la salud esta al maximo
                        if salud_enemigo + curacion >= self.__vida_enemigo:
                            curacion = self.__vida_enemigo - salud_enemigo
                            salud_enemigo = self.__vida_enemigo
                        else:
                            salud_enemigo += curacion
                        print(
                            f"El enemigo uso curacion pequeña, se curo un total de {curacion} total usos: {maximo_curacion}\n"
                            + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                        )
                        input(
                            "       ------  Presione enter para continuar  ------       "
                        )
                        id.limpiar_pantalla()
                    elif turno_enemigo == 24 or turno_enemigo == 25:
                        # opcion en la que usa curacion grande
                        curacion = int(
                            self.__curacion_grande
                            + random.randint(5, 9)
                            + (self.__vida_enemigo * 0.18)
                        )
                        maximo_curacion -= 1
                        # si la salud esta al maximo
                        if salud_enemigo + curacion >= self.__vida_enemigo:
                            curacion = self.__vida_enemigo - salud_enemigo
                            salud_enemigo = self.__vida_enemigo
                        else:
                            salud_enemigo += curacion
                        print(
                            f"El enemigo uso curacion grande, se curo un total de {curacion} total usos: {maximo_curacion}\n"
                            + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                        )
                        input(
                            "       ------  Presione enter para continuar  ------       "
                        )
                        id.limpiar_pantalla()
        else:
            # para cuando no se encontro enemigos
            print("No se encontro enemigos")
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()

    # metodo atacar del personaje
    def atacar(self, opcion, salud_enemigo, salud_personaje, usos):
        probabilidad_critico = False
        critico = random.randint(1, 15)
        frase_golpe = "ataca"
        # probabilidad de 46.7 por ciento de que salga golpe critico con puño
        if critico >= 4 and critico <= 10 and opcion == 1:
            # el daño es basado en el 33 por ciento del daño del personaje
            self.__probabilidad_golpe_critico_personaje = int(
                self.__daño_personaje * 0.333
            )
            frase_golpe = "ataca con ¡Golpe Critico!"
        # probabilidad de 20 por ciento de que salga golpe critico con espada
        elif critico >= 4 and critico <= 6 and opcion == 2:
            # el daño es basado en el 27 por ciento del daño del personaje
            self.__probabilidad_golpe_critico_personaje = int(
                self.__daño_personaje * 0.27
            )
            frase_golpe = "hizo un ¡Golpe Critico!"
        # probabilidad de 33.333 por ciento de que salga golpe critico con espada
        elif critico >= 4 and critico <= 8 and opcion == 3:
            # el daño es basado en el 30 por ciento del daño del personaje
            self.__probabilidad_golpe_critico_personaje = int(
                self.__daño_personaje * 0.3
            )
            frase_golpe = "hizo un ¡Golpe Critico!"
        else:
            # si no hay probabilidad de golpe critico
            self.__probabilidad_golpe_critico_personaje = 0
        if opcion == 1:
            # opcion ataque con puños
            daño = (
                self.__daño_personaje
                + random.randint(self.__fuerza_personaje, (2 + self.__fuerza_personaje))
                + self.__probabilidad_golpe_critico_personaje
            )
            salud_enemigo -= daño
            if salud_enemigo < 0:
                salud_enemigo = 0
            print(
                f"{self.__nombre_personaje} {frase_golpe}, hizo un daño de {daño}\n"
                + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
            )
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
        elif opcion == 2:
            # opcion ataque con espada
            daño = (
                self.__daño_personaje
                + random.randint(
                    self.__fuerza_personaje + self.__espada,
                    (2 + self.__fuerza_personaje + self.__espada),
                )
                + self.__probabilidad_golpe_critico_personaje
            )
            salud_enemigo -= daño
            usos[0] -= 1
            if salud_enemigo < 0:
                salud_enemigo = 0
            print(
                f"{self.__nombre_personaje} {frase_golpe} con espada, hizo un daño de {daño}\n"
                + f"   ------ Usos restantes de espada: {usos[0]} ------\n"
                + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
            )
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
        elif opcion == 3:
            # opcion ataque con hacha
            daño = (
                self.__daño_personaje
                + random.randint(
                    self.__fuerza_personaje + self.__hacha,
                    (2 + self.__fuerza_personaje + self.__hacha),
                )
                + self.__probabilidad_golpe_critico_personaje
            )
            salud_enemigo -= daño
            usos[1] -= 1
            if salud_enemigo < 0:
                salud_enemigo = 0
            print(
                f"{self.__nombre_personaje} {frase_golpe} con hacha, hizo un daño de {daño}\n"
                + f"   ------ Usos restantes de hacha: {usos[1]} ------\n"
                + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
            )
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
        elif opcion == 4:
            # opcion curacion
            if self.__curacion_personaje > 0:
                self.__curacion_personaje -= 1
                # lo que se va a curar el personaje
                curacion = int(
                    self.__curacion
                    + random.randint(1, 5)
                    + (self.__salud_personaje * 0.16)
                )
                if salud_personaje + curacion >= self.__salud_personaje:
                    curacion = self.__salud_personaje - salud_personaje
                    salud_personaje = self.__salud_personaje
                else:
                    salud_personaje += curacion
                print(
                    f"{self.__nombre_personaje} uso curacion, se curo un total de {curacion}\n"
                    + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                )
            else:
                # si ya no tiene curaciones
                print(
                    f"{self.__nombre_personaje} no tiene mas curaciones el turno se perdio en tratar de encontrar uno\n"
                    + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                )
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
        elif opcion == 5:
            # opcion curacion grande
            if self.__curacion_grande_personaje > 0:
                self.__curacion_grande_personaje -= 1
                # lo que se va a curar el personaje
                curacion = int(
                    self.__curacion_grande
                    + random.randint(5, 10)
                    + (self.__salud_personaje * 0.19)
                )
                if salud_personaje + curacion >= self.__salud_personaje:
                    curacion = self.__salud_personaje - salud_personaje
                    salud_personaje = self.__salud_personaje
                else:
                    salud_personaje += curacion
                print(
                    f"{self.__nombre_personaje} uso curacion grande, se curo un total de {curacion}\n"
                    + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                )
            else:
                # si ya no tiene curaciones
                print(
                    f"{self.__nombre_personaje} no tiene mas curaciones el turno se perdio en tratar de encontrar uno\n"
                    + f"Personaje: {salud_personaje}   Enemigo: {salud_enemigo}"
                )
            input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
        # verifica que salud cambia dependiendo de la accion del personaje
        if opcion >= 1 and opcion <= 3:
            return salud_enemigo
        else:
            return salud_personaje

    # metodo para usar un item en la pelea
    def usar(self, ronda, usos):
        opcion = 0
        espada_rota = False
        hacha_rota = False
        # verifica el estado de las armas
        if usos[0] <= 0:
            espada_rota = True
        if usos[1] <= 0:
            hacha_rota = True
        # entra al bucle solo si las armas estan rotas y elige esa opcion de atacar con hacha o espada
        while (
            ((espada_rota or not (self.__tiene_espada)) and opcion == 2)
            or ((hacha_rota or not (self.__tiene_hacha)) and opcion == 3)
            or opcion == 0
        ):
            # elige que accion quiere tomar
            print(
                f"Ronda: {ronda}\n"
                + "1 Para atacar con puños (tiene mas probabilidad de golpe critico)\n"
                + "2 Para atacar con espada (tiene menos probabilidad de golpe critico)\n"
                + "3 Para atacar con hacha (probabilidad de golpe critico normal)\n"
                + "4 Para usar curacion\n"
                + "5 Para usar curacion grande\n"
                + "6 Para escapar"
            )
            opcion = id.num_entero("Accion:")
            # si aun no tiene hacha
            if not (self.__tiene_hacha) and opcion == 3:
                print(" - No tienes una hacha")
                input("       ------  Presione enter para continuar  ------       ")
            # si aun no tiene espada
            elif not (self.__tiene_espada) and opcion == 2:
                print(" - No tienes una espada")
                input("       ------  Presione enter para continuar  ------       ")
            # si elige espada y esta rota
            elif espada_rota and opcion == 2:
                print("  ------  La espada esta rota ya no puedes usarla  ------ ")
                input("       ------  Presione enter para continuar  ------       ")
            # si elige hacha y esta rota
            elif hacha_rota and opcion == 3:
                print("  ------  La hacha esta rota ya no puedes usarla  ------ ")
                input("       ------  Presione enter para continuar  ------       ")
            id.limpiar_pantalla()
        return opcion

    # metodo para mostrar barra de progreso
    def barra_progreso(self, validar_subir_nivel, validar_nivel_maximo, validar):
        frase = "|"
        retorno = ""
        # se divide para atributo validar para los guiones
        for progreso in range((self.__exp_personaje // self.__validar) + 1):
            # en múltiplo de 3 aumenta en 2 la barra de progreso
            if progreso % 3 == 0 and validar and progreso != 0:
                frase += "||"
                # cuando sube de exp pero no sube de nivel
                retorno = (
                    "    ______________________________________________________________________\n"
                    + f"    {frase}\n"
                    + "    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
                )
            # cuando sube de nivel
            elif validar_subir_nivel:
                return (
                    "    ______________________________________________________________________\n"
                    + "    ||||||||||||||||||||||||||| Subiste de Nivel |||||||||||||||||||||||||\n"
                    + "    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
                )
            # cuando llega al nivel maximo
            elif validar_nivel_maximo:
                # para que ya no tenga mas experiencia
                self.__exp_personaje = 0
                return (
                    "    ______________________________________________________________________\n"
                    + "    ||||||||||||||||||||||||||||| Nivel Maximo |||||||||||||||||||||||||||\n"
                    + "    ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯"
                )
        return retorno

    # probabilidad de anillo
    def probabilidad_objeto(self):
        toda_frase = ""
        # probabilidad de que te den el anillo del 3 por ciento
        suerte_anillo = random.randint(1, 100)
        if suerte_anillo >= 3 and suerte_anillo <= 5:
            # para que solo lo consiga una vez
            if self.__anillo_inmortal == 0:
                self.__anillo_inmortal = 1
                self.__frase_anillo = " - Posees un anillo de la inmortalidad"
                toda_frase += (
                    "\n     ----- ¡Felicidades! conseguiste un anillo de inmortalidad -----\n"
                    + "    ----- solo hay uno en este mundo y te ayudara en tu aventura -----"
                )
        # probabilidad de conseguir hacha
        suerte_hacha = random.randint(1, 20)
        # suerte del 25 por ciento
        if suerte_hacha >= 3 and suerte_hacha <= 7 and not (self.__tiene_hacha):
            self.__tiene_hacha = True
            self.__uso_hacha = 6
            toda_frase += "\n     ---- Haz conseguido una hacha ----"
        # probabilidad de conseguir espada
        suerte_espada = random.randint(1, 30)
        if (
            suerte_espada >= 10
            and suerte_espada <= 15
            and self.__tiene_hacha
            and not (self.__tiene_espada)
        ):
            self.__tiene_espada = True
            self.__uso_espada = 6
            toda_frase += "\n     ---- Haz conseguido una espada ----"
        return toda_frase


# se crea el objeto Juego
juego = Juego()
juego.nombre_personaje = input("Ingrese el nombre del jugador: ")
# simulacion de carga del modulo ingresar datos
juego.cargando("¡Cargando Juego!", "¡Juego cargado con exito!", 0.92)
# bienvenida del jugador
print(
    "    ------       Bienvenido a esta aventura       ------\n"
    + f"Hola {juego.nombre_personaje} tu objetivo es convertirte en el mas fuerte\n"
    + "Ha medida que avances en tu aventura seras mas fuerte y encontraras enemigos\n"
    + "cada vez mas temidos\n"
    + "Suerte aventurero"
)
# bucle del juego
while not (juego.game_over):
    # se da casos de caminos de forma aleatoria
    camino = random.randint(1, 3)
    opcion = 6
    if camino == 1:
        # verifica la opcion que elige el personaje
        while opcion < 1 or opcion > 5 or opcion == 4:
            print(
                "1 Para ir a la izquierda\n"
                + "2 Para ir a la derecha\n"
                + "3 Para ir hacia adelante\n"
                + "4 Para ver estadisticas\n"
                + "5 Abandonar la aventura"
            )
            opcion = id.num_entero("Accion:")
            if opcion < 1 or opcion > 5:
                print("Debe escoger una de las opciones dadas")
                input("       ------  Presione enter para continuar  ------       ")
                id.limpiar_pantalla()
            else:
                juego.mover(opcion)
    elif camino == 2:
        # verifica la opcion que elige el personaje
        while opcion < 3 or opcion > 5 or opcion == 4:
            print(
                "1 Camino de la izquierda bloqueado\n"
                + "2 Camino de la derecha bloqueado\n"
                + "3 Para ir hacia adelante\n"
                + "4 Para ver estadisticas\n"
                + "5 Abandonar la aventura"
            )
            opcion = id.num_entero("Accion:")
            if opcion < 3 or opcion > 5:
                print("Debe escoger una de las opciones dadas")
                input("       ------  Presione enter para continuar  ------       ")
                id.limpiar_pantalla()
            else:
                juego.mover(opcion)
    elif camino == 3:
        # verifica la opcion que elige el personaje
        while opcion < 1 or opcion > 5 or opcion == 2 or opcion == 3 or opcion == 4:
            print(
                "1 Para ir a la izquierda\n"
                + "2 Camino de la derecha bloqueado\n"
                + "3 Camino de adelante bloqueado\n"
                + "4 Para ver estadisticas\n"
                + "5 Abandonar la aventura"
            )
            opcion = id.num_entero("Accion:")
            if opcion < 1 or opcion > 5 or opcion == 2 or opcion == 3:
                print("Debe escoger una de las opciones dadas")
                input("       ------  Presione enter para continuar  ------       ")
                id.limpiar_pantalla()
            else:
                juego.mover(opcion)
