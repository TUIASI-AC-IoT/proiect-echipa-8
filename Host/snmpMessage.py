from pyasn1.codec.ber import encoder, decoder
from pyasn1.type import univ, namedtype

def encodeASN1(oid, text):

    #snmp message
    pdu = univ.Sequence(componentType=namedtype.NamedTypes(
        namedtype.NamedType('request-id', univ.Integer(123)),
        namedtype.NamedType('error-status', univ.Integer(0)),
        namedtype.NamedType('error-index', univ.Integer(0)),
        namedtype.NamedType('variable-bindings', univ.Sequence(componentType=namedtype.NamedTypes(
        namedtype.NamedType('name', univ.ObjectIdentifier((oid))),
        namedtype.NamedType('value', univ.Null('')),
        namedtype.NamedType('value', univ.OctetString(text))
        )))
        ))

    #Encode the PDU using BER
    encoded_pdu = encoder.encode(pdu)

    snmp_message = univ.Sequence(componentType=namedtype.NamedTypes(
        namedtype.NamedType('version', univ.Integer(0)),
        namedtype.NamedType('community', univ.OctetString('public')),
        namedtype.NamedType('data', pdu)
    ))

    #Encode the message
    encoded_message = encoder.encode(snmp_message)

    return encoded_message

def decodeASN1(message):

    snmp_message = None
    snmp_message, _ = decoder.decode(message, asn1Spec= snmp_message)
    pdu = snmp_message[2]
    variable_bindings = pdu[3]
    variable_binding = variable_bindings[0]
    oid = variable_binding[0]
    oid1=variable_binding[1]

    return variable_bindings