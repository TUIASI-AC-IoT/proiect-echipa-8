from pyasn1.type import univ, namedtype, namedval
from pyasn1.type.univ import Real
from pyasn1.codec.ber import encoder, decoder

def encodeASN1(oid, text, val):

    pdu = univ.Sequence(componentType=namedtype.NamedTypes(
        namedtype.NamedType('request-id', univ.Integer(123)),
        namedtype.NamedType('error-status', univ.Integer(0)),
        namedtype.NamedType('error-index', univ.Integer(0)),
        namedtype.NamedType('variable-bindings', univ.Sequence(componentType=namedtype.NamedTypes(
            namedtype.NamedType('name', univ.ObjectIdentifier(oid)),
            namedtype.NamedType('value', univ.OctetString(text)),
            namedtype.NamedType('value', univ.Real(val))
        )))
    ))

    encoded_pdu = encoder.encode(pdu)

    snmp_message = univ.Sequence(componentType=namedtype.NamedTypes(
        namedtype.NamedType('version', univ.Integer(0)),
        namedtype.NamedType('community', univ.OctetString('public')),
        namedtype.NamedType('data', pdu)
    ))

    encoded_message = encoder.encode(snmp_message)

    return encoded_message

def decodeASN1(encoded_message):

    snmp_message = None
    snmp_message, _ = decoder.decode(encoded_message, asn1Spec=snmp_message)
    pdu=snmp_message[2]
    variable_bindings = pdu[3]
    variable_binding=variable_bindings[0]

    return variable_bindings