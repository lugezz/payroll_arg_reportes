FORMATO_TXT_F931 = {
    'cuil': {'from': 1, 'long': 11},
    'nombre_completo': {'from': 12, 'long': 30},
    'conyuge': {'from': 42, 'long': 1},
    'hijos': {'from': 43, 'long': 2},
    'situacion': {'from': 45, 'long': 2},
    'condicion': {'from': 47, 'long': 2},
    'actividad': {'from': 49, 'long': 3},
    'zona': {'from': 52, 'long': 2},
    'porcentaje_aporte_adicional_ss': {'from': 54, 'long': 5},
    'modalidad_contrato': {'from': 59, 'long': 3},
    'obra_social': {'from': 62, 'long': 6},
    'adherentes': {'from': 68, 'long': 2},
    'remuneracion_total': {'from': 70, 'long': 12},
    'remuneracion_01': {'from': 82, 'long': 12},
    'asignaciones_familiares': {'from': 94, 'long': 9},
    'aporte_vol': {'from': 103, 'long': 9},
    'importe_adicional_os': {'from': 112, 'long': 9},
    'imp_exc_ap_ss': {'from': 121, 'long': 9},
    'imp_exc_ap_os': {'from': 130, 'long': 9},
    'provincia_localidad': {'from': 139, 'long': 50},
    'remuneracion_02': {'from': 189, 'long': 12},
    'remuneracion_03': {'from': 201, 'long': 12},
    'remuneracion_04': {'from': 213, 'long': 12},
    'codigo_siniestrado': {'from': 225, 'long': 2},
    'marca_corresponde_reduccion': {'from': 227, 'long': 1},
    'capital_lrt': {'from': 228, 'long': 9},
    'tipo_empresa': {'from': 237, 'long': 1},
    'aporte_adicional_obra_social': {'from': 238, 'long': 9},
    'regimen': {'from': 247, 'long': 1},
    'situacion_1': {'from': 248, 'long': 2},
    'dia_sr1': {'from': 250, 'long': 2},
    'situacion_2': {'from': 252, 'long': 2},
    'dia_sr2': {'from': 254, 'long': 2},
    'situacion_3': {'from': 256, 'long': 2},
    'dia_sr3': {'from': 258, 'long': 2},
    'sueldo': {'from': 260, 'long': 12},
    'sac': {'from': 272, 'long': 12},
    'hs_extras': {'from': 284, 'long': 12},
    'zona_desfavorable': {'from': 296, 'long': 12},
    'vacaciones': {'from': 308, 'long': 12},
    'k_dias': {'from': 320, 'long': 9},
    'remuneracion_05': {'from': 329, 'long': 12},
    'trabajador_convencionado': {'from': 341, 'long': 1},
    'remuneracion_06': {'from': 342, 'long': 12},
    'tipo_operacion': {'from': 354, 'long': 1},
    'adicionales': {'from': 355, 'long': 12},
    'premios': {'from': 367, 'long': 12},
    'remuneracion_08': {'from': 379, 'long': 12},
    'remuneracion_07': {'from': 391, 'long': 12},
    'k_hs_extras': {'from': 403, 'long': 3},
    'no_remunerativo': {'from': 406, 'long': 12},
    'maternidad': {'from': 418, 'long': 12},
    'rectificacion': {'from': 430, 'long': 9},
    'remuneracion_09': {'from': 439, 'long': 12},
    'porc_contr_dif_ss': {'from': 451, 'long': 9},
    'k_horas': {'from': 460, 'long': 3},
    'seguro_vida_obligatorio': {'from': 463, 'long': 1},
    'detraccion': {'from': 464, 'long': 12},
    'incremento': {'from': 476, 'long': 12},
    'remuneracion_11': {'from': 488, 'long': 12},
}


def get_value_from_txt(txt_line: str, field_name: str) -> str:
    """ Retorna el valor de un campo en un txt de F931 de acuerdo a las
        posiciones del campo en el txt detalladas en FORMATO_TXT_F931
    """
    resp = ''

    if field_name in FORMATO_TXT_F931:
        resp = txt_line[FORMATO_TXT_F931[field_name]['from'] - 1:FORMATO_TXT_F931[field_name]['from'] - 1 +
                        FORMATO_TXT_F931[field_name]['long']].strip()

    return resp


def amount_txt_to_integer(amount_txt: str, mulitp=100) -> int:
    """ Convierte un monto en formato de texto a entero
    """
    resp = float(amount_txt.replace(',', '.')) * mulitp
    resp = int(resp)

    return resp


def amount_txt_to_float(amount_txt: str, multip: int = 100, rount_to: int = 2) -> float:
    """ Convierte un monto en formato de texto a float
    """
    resp = float(amount_txt.replace(',', '.')) * multip
    resp = float(resp)
    resp = round(resp, rount_to)

    return resp


def sync_format(info: str, expected_len: int, type_info: str, multiplicador: int = 1) -> str:
    """ Sincroniza el formato de un campo de un txt de F931
        Args:
            info: str, valor del campo
            expected_len: int, longitud esperada del campo
            type_info: str, tipo de campo (NU - Numérico, AL - Alfabético, AN - Alfanumérico)
            multiplicador: int, multiplicador del campo
    """
    resp = info

    if len(info) != expected_len or ',' in info:
        if len(info) > expected_len:
            resp = round(float(info.replace(',', '.').strip()))
            # Ver si está ok multiplicar por 100
            resp = str(resp * multiplicador).zfill(expected_len)
        else:
            if type_info == 'NU':
                resp = str(int(float(info.replace(',', '.').strip()) * 100))
                resp = resp.zfill(expected_len)
            else:
                resp = info.ljust(expected_len)

    return resp