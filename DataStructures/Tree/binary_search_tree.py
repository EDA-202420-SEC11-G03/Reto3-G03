from DataStructures.Tree import bst_node as bn
from DataStructures.List import array_list as al

def new_map():
    
    return {
        "root": None,
        "type": "BST"
    }
    
def insert_node(root, key, value):
    """Inserta un nodo en el árbol binario
    
    :param my_map: El árbol binario
    :type my_map: dict
    :param key: Llave del nodo a insertar
    :type key: any
    :param value: Valor del nodo a insertar
    :type value: any
    """
    
    if root is None:
        return bn.new_node(key, value)
    elif key == bn.get_key(root):
        root["value"] = value
    elif key < bn.get_key(root):
        root["left"] = insert_node(root["left"], key, value)
    else:
        root["right"] = insert_node(root["right"], key, value)
    
    root["size"] = bn.get_size(root)
        
    return root

def put(my_map, key, value):
    """Inserta un nodo en el árbol binario
    
    :param my_map: El árbol binario
    :type my_map: dict
    :param key: Llave del nodo a insertar
    :type key: any
    :param value: Valor del nodo a insertar
    :type value: any
    """
    my_map["root"] = insert_node(my_map["root"], key, value)
    
    return my_map

def get(my_bst, key):
    """Retorna el valor asociado a una llave
    
    :param my_bst: El árbol binario
    :type my_bst: dict
    :param key: Llave del nodo a buscar
    :type key: any
    
    :returns: El valor asociado a la llave
    :rtype: any
    """
    root = my_bst["root"]
    
    return get_node(root, key)
    
def get_node(root, key):
    """Retorna el nodo asociado a una llave
    
    :param root: El nodo raíz
    :type root: dict
    :param key: Llave del nodo a buscar
    :type key: any
    
    :returns: El nodo asociado a la llave
    :rtype: dict
    """
    if root is not None:
        if key == bn.get_key(root):
            return bn.get_value(root)
        if key < bn.get_key(root):
            return get_node(root["left"], key)
        if key > bn.get_key(root):
            return get_node(root["right"], key)
        
def contains(my_map, key):
    """Retorna True si la llave está en el árbol
    
    :param my_map: El árbol binario
    :type my_map: dict
    :param key: Llave del nodo a buscar
    :type key: any
    
    :returns: True si la llave está en el árbol
    :rtype: bool
    """
    return get(my_map, key) is not None

def size(my_map):
    """Retorna el tamaño del árbol
    
    :param my_map: El árbol binario
    :type my_map: dict
    
    :returns: El tamaño del árbol
    :rtype: int
    """
    return bn.get_size(my_map["root"])

def is_empty(my_map):
    """Retorna True si el árbol está vacío
    
    :param my_map: El árbol binario
    :type my_map: dict
    
    :returns: True si el árbol está vacío
    :rtype: bool
    """
    return my_map["root"] is None

def key_set(my_map):
    """Retorna el conjunto de llaves del árbol
    
    :param my_map: El árbol binario
    :type my_map: dict
    
    :returns: El conjunto de llaves del árbol
    :rtype: list
    """
    set = al.new_list()
    
    keys = key_set_node(my_map["root"], set)
    
    return keys

def key_set_node(root, keys):
    
    if root is not None:
        key_set_node(root["left"], keys)
        if al.is_present(keys, bn.get_key(root), al.default_function) == -1:
            al.add_last(keys, bn.get_key(root))
        key_set_node(root["right"], keys)
        
    return keys

def value_set(my_map):
    """Retorna el conjunto de valores del árbol
    
    :param my_map: El árbol binario
    :type my_map: dict
    
    :returns: El conjunto de valores del árbol
    :rtype: list
    """
    set = al.new_list()
    
    values = value_set_node(my_map["root"], set)
    
    return values

def value_set_node(root, values):
    
    if root is not None:
        value_set_node(root["left"], values)
        if al.is_present(values, bn.get_value(root), al.default_function) == -1:
            al.add_last(values, bn.get_value(root))
        value_set_node(root["right"], values)
        
    return values
    
def min_key(my_map):
    """Retorna la llave mínima del árbol
    
    :param my_map: El árbol binario
    :type my_map: dict
    
    :returns: La llave mínima del árbol
    :rtype: any
    """
    root = my_map["root"]
    
    return min_key_node(root)

def min_key_node(root):
        
    if root is not None:
        if root["left"] is None:
            return bn.get_key(root)
        return min_key_node(root["left"])

def max_key(my_map):
    """Retorna la llave máxima del árbol
    
    :param my_map: El árbol binario
    :type my_map: dict
    
    :returns: La llave máxima del árbol
    :rtype: any
    """
    root = my_map["root"]
    
    return max_key_node(root)

def max_key_node(root):
        
    if root is not None:
        if root["right"] is None:
            return bn.get_key(root)
        return max_key_node(root["right"])
    
def floor(my_bst, key):
    """Retorna la llave más grande menor o igual a la llave dada
    
    :param my_bst: El árbol binario
    :type my_bst: dict
    :param key: La llave a buscar
    :type key: any
    
    :returns: La llave más grande menor o igual a la llave dada
    :rtype: any
    """
    root = my_bst["root"]
    
    return floor_node(root, key)

def floor_node(root, key):
        
    if root is not None:
        if key == bn.get_key(root):
            return bn.get_key(root)
        if key < bn.get_key(root):
            return floor_node(root["left"], key)
        t = floor_node(root["right"], key)
        if t is not None:
            return t
        return bn.get_key(root)
    
def ceiling(my_bst, key):
    """Retorna la llave más pequeña mayor o igual a la llave dada
    
    :param my_bst: El árbol binario
    :type my_bst: dict
    :param key: La llave a buscar
    :type key: any
    
    :returns: La llave más pequeña mayor o igual a la llave dada
    :rtype: any
    """
    root = my_bst["root"]
    
    return ceiling_node(root, key)
        
def ceiling_node(root, key):
            
        if root is not None:
            if key == bn.get_key(root):
                return bn.get_key(root)
            if key > bn.get_key(root):
                return ceiling_node(root["right"], key)
            t = ceiling_node(root["left"], key)
            if t is not None:
                return t
            return bn.get_key(root)
        
def rank(my_bst, key):

    root = my_bst["root"]
    
    return rank_node(root, key)

def rank_node(root, key):
        
        if root is None:
            return 0
        if key < bn.get_key(root):
            return rank_node(root["left"], key)
        if key > bn.get_key(root):
            return 1 + bn.get_size(root["left"]) + rank_node(root["right"], key)
        return bn.get_size(root["left"])
    
def keys_range(root, key_lo, key_hi, list_key):
    if root is None:
        return
    if key_lo< root["key"]:
        keys_range(root["left"], key_lo, key_hi, list_key)
    if key_lo <= root["key"] <= key_hi:
        al.add_last(list_key, root["key"])
    if key_hi> root["key"]:
        keys_range(root["right"], key_lo, key_hi, list_key) 
def keys (my_bst, key_lo, key_hi):
    list_key= al.new_list()
    keys_range(my_bst["root"], key_lo, key_hi, list_key)
    return list_key


def values_range(root, key_lo, key_hi, list_values):
    if root is None:
        return
    if key_lo< root["key"]:
        values_range(root["left"], key_lo, key_hi, list_values)
    if key_lo <= root["key"] <= key_hi:
        al.add_last(list_values, root["value"])
    if key_hi> root["key"]:
        values_range(root["right"], key_lo, key_hi, list_values) 
def values (my_bst, key_lo, key_hi):
    list_values= al.new_list()
    values_range(my_bst["root"], key_lo, key_hi, list_values)
    return list_values
def height_tree(root):
    if root is None:
        return -1  
    else:
        altura_izquierda = height_tree(root["left"])
        altura_derecha = height_tree(root["right"])

        return 1 + max(altura_izquierda, altura_derecha)
def height(my_bst):
    altura= height_tree(my_bst["root"])
    return altura