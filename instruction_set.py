instructions = {

    0x00: 'nop',
    0x01: 'ld bc,d16',
    0x02: 'ld [bc],a',
    0x03: 'inc bc',
    0x04: 'inc b',
    0x05: 'dec b',
    0x06: 'ld b,d8',
    0x07: 'rlca',
    0x08: 'ld [a16],sp',
    0x09: 'add hl,bc',
    0x0a: 'ld a,[bc]',
    0x0b: 'dec bc',
    0x0c: 'inc c',
    0x0d: 'dec c',
    0x0e: 'ld c,d8',
    0x0f: 'rrca',

    0x10: 'stop',
    0x11: 'ld de,d16',
    0x12: 'ld [de],a',
    0x13: 'inc de',
    0x14: 'inc d',
    0x15: 'dec d',
    0x16: 'ld d,d8',
    0x17: 'rla',
    0x18: 'jr pc+r8',
    0x19: 'add hl,de',
    0x1a: 'ld a,[de]',
    0x1b: 'dec de',
    0x1c: 'inc e',
    0x1d: 'dec e',
    0x1e: 'ld e,d8',
    0x1f: 'rra',

    0x20: 'jr nz,pc+r8',
    0x21: 'ld hl,d16',
    0x22: 'ld [hl+],a',
    0x23: 'inc hl',
    0x24: 'inc h',
    0x25: 'dec h',
    0x26: 'ld h,d8',
    0x27: 'daa',
    0x28: 'jr z,pc+r8',
    0x29: 'add hl,hl',
    0x2a: 'ld a,[hl+]',
    0x2b: 'dec hl',
    0x2c: 'inc l',
    0x2d: 'dec l',
    0x2e: 'ld l,d8',
    0x2f: 'cpl',

    0x30: 'jr nc,pc+r8',
    0x31: 'ld sp,d16',
    0x32: 'ld [hl-],a',
    0x33: 'inc sp',
    0x34: 'inc [hl]',
    0x35: 'dec [hl]',
    0x36: 'ld [hl],d8',
    0x37: 'scf',
    0x38: 'jr c,pc+r8',
    0x39: 'add hl,sp',
    0x3a: 'ld a,[hl-]',
    0x3b: 'dec sp',
    0x3c: 'inc a',
    0x3d: 'dec a',
    0x3e: 'ld a,d8',
    0x3f: 'ccf',

    0x40: 'ld b,b',
    0x41: 'ld b,c',
    0x42: 'ld b,d',
    0x43: 'ld b,e',
    0x44: 'ld b,h',
    0x45: 'ld b,l',
    0x46: 'ld b,[hl]',
    0x47: 'ld b,a',
    0x48: 'ld c,b',
    0x49: 'ld c,c',
    0x4a: 'ld c,d',
    0x4b: 'ld c,e',
    0x4c: 'ld c,h',
    0x4d: 'ld c,l',
    0x4e: 'ld c,[hl]',
    0x4f: 'ld c,a',

    0x50: 'ld d,b',
    0x51: 'ld d,c',
    0x52: 'ld d,d',
    0x53: 'ld d,e',
    0x54: 'ld d,h',
    0x55: 'ld d,l',
    0x56: 'ld d,[hl]',
    0x57: 'ld d,a',
    0x58: 'ld e,b',
    0x59: 'ld e,c',
    0x5a: 'ld e,d',
    0x5b: 'ld e,e',
    0x5c: 'ld e,h',
    0x5d: 'ld e,l',
    0x5e: 'ld e,[hl]',
    0x5f: 'ld e,a',

    0x60: 'ld h,b',
    0x61: 'ld h,c',
    0x62: 'ld h,d',
    0x63: 'ld h,e',
    0x64: 'ld h,h',
    0x65: 'ld h,l',
    0x66: 'ld h,[hl]',
    0x67: 'ld h,a',
    0x68: 'ld l,b',
    0x69: 'ld l,c',
    0x6a: 'ld l,d',
    0x6b: 'ld l,e',
    0x6c: 'ld l,h',
    0x6d: 'ld l,l',
    0x6e: 'ld l,[hl]',
    0x6f: 'ld l,a',

    0x70: 'ld [hl],b',
    0x71: 'ld [hl],c',
    0x72: 'ld [hl],d',
    0x73: 'ld [hl],e',
    0x74: 'ld [hl],h',
    0x75: 'ld [hl],l',
    0x76: 'halt',
    0x77: 'ld [hl],a',
    0x78: 'ld a,b',
    0x79: 'ld a,c',
    0x7a: 'ld a,d',
    0x7b: 'ld a,e',
    0x7c: 'ld a,h',
    0x7d: 'ld a,l',
    0x7e: 'ld a,[hl]',
    0x7f: 'ld a,a',

    0x80: 'add b',
    0x81: 'add c',
    0x82: 'add d',
    0x83: 'add e',
    0x84: 'add h',
    0x85: 'add l',
    0x86: 'add [hl]',
    0x87: 'add a',
    0x88: 'adc b',
    0x89: 'adc c',
    0x8a: 'adc d',
    0x8b: 'adc e',
    0x8c: 'adc h',
    0x8d: 'adc l',
    0x8e: 'adc [hl]',
    0x8f: 'adc a',    

    0x90: 'sub b',
    0x91: 'sub c',
    0x92: 'sub d',
    0x93: 'sub e',
    0x94: 'sub h',
    0x95: 'sub l',
    0x96: 'sub [hl]',
    0x97: 'sub a',
    0x98: 'sbc b',
    0x99: 'sbc c',
    0x9a: 'sbc d',
    0x9b: 'sbc e',
    0x9c: 'sbc h',
    0x9d: 'sbc l',
    0x9e: 'sbc [hl]',
    0x9f: 'sbc a',

    0xa0: 'and b',
    0xa1: 'and c',
    0xa2: 'and d',
    0xa3: 'and e',
    0xa4: 'and h',
    0xa5: 'and l',
    0xa6: 'and [hl]',
    0xa7: 'and a',
    0xa8: 'xor b',
    0xa9: 'xor c',
    0xaa: 'xor d',
    0xab: 'xor e',
    0xac: 'xor h',
    0xad: 'xor l',
    0xae: 'xor [hl]',
    0xaf: 'xor a',

    0xb0: 'or b',
    0xb1: 'or c',
    0xb2: 'or d',
    0xb3: 'or e',
    0xb4: 'or h',
    0xb5: 'or l',
    0xb6: 'or [hl]',
    0xb7: 'or a',
    0xb8: 'cp b',
    0xb9: 'cp c',
    0xba: 'cp d',
    0xbb: 'cp e',
    0xbc: 'cp h',
    0xbd: 'cp l',
    0xbe: 'cp [hl]',
    0xbf: 'cp a',

    0xc0: 'ret nz',
    0xc1: 'pop bc',
    0xc2: 'jp nz,a16',
    0xc3: 'jp a16',
    0xc4: 'call nz,a16',
    0xc5: 'push bc',
    0xc6: 'add d8',
    0xc7: 'rst $00',
    0xc8: 'ret z',
    0xc9: 'ret',
    0xca: 'jp z,a16',
    0xcb: 'CBPREFIX',
    0xcc: 'call z,a16',
    0xcd: 'call a16',
    0xce: 'adc d8',
    0xcf: 'rst $08',

    0xd0: 'ret nc',
    0xd1: 'pop de',
    0xd2: 'jp nc,a16',
    0xd3: 'DB $d3',
    0xd4: 'call nc,a16',
    0xd5: 'push de',
    0xd6: 'sub d8',
    0xd7: 'rst $10',
    0xd8: 'ret c',
    0xd9: 'reti',
    0xda: 'jp c,a16',
    0xdb: 'DB $db',
    0xdc: 'call c,a16',
    0xdd: 'DB $dd',
    0xde: 'sbc d8',
    0xdf: 'rst $18',

    0xe0: 'ld [$ff00+a8],a',
    0xe1: 'pop hl',
    0xe2: 'ld [$ff00+c],a',
    0xe3: 'DB $e3',
    0xe4: 'DB $e4',
    0xe5: 'push hl',
    0xe6: 'and d8',
    0xe7: 'rst $20',
    0xe8: 'add sp,r8',
    0xe9: 'jp hl',
    0xea: 'ld [a16],a',
    0xeb: 'DB $eb',
    0xec: 'DB $ec',
    0xed: 'DB $ed',
    0xee: 'xor d8',
    0xef: 'rst $28',

    0xf0: 'ld a,[$ff00+a8]',
    0xf1: 'pop af',
    0xf2: 'ld a,[$ff00+c]',
    0xf3: 'di',
    0xf4: 'DB $f4',
    0xf5: 'push af',
    0xf6: 'or d8',
    0xf7: 'rst $30',
    0xf8: 'ld hl,sp+r8',
    0xf9: 'ld sp,hl',
    0xfa: 'ld a,[a16]',
    0xfb: 'ei',
    0xfc: 'DB $fc',
    0xfd: 'DB $fd',
    0xfe: 'cp d8',
    0xff: 'rst $38',

}

cb_instructions = {
    
    0x00: 'rlc b',
    0x01: 'rlc c',
    0x02: 'rlc d',
    0x03: 'rlc e',
    0x04: 'rlc h',
    0x05: 'rlc l',
    0x06: 'rlc [hl]',
    0x07: 'rlc a',
    0x08: 'rrc b',
    0x09: 'rrc c',
    0x0a: 'rrc d',
    0x0b: 'rrc e',
    0x0c: 'rrc h',
    0x0d: 'rrc l',
    0x0e: 'rrc [hl]',
    0x0f: 'rrc a',
    
    0x10: 'rl b',
    0x11: 'rl c',
    0x12: 'rl d',
    0x13: 'rl e',
    0x14: 'rl h',
    0x15: 'rl l',
    0x16: 'rl [hl]',
    0x17: 'rl a',
    0x18: 'rr b',
    0x19: 'rr c',
    0x1a: 'rr d',
    0x1b: 'rr e',
    0x1c: 'rr h',
    0x1d: 'rr l',
    0x1e: 'rr [hl]',
    0x1f: 'rr a',
    
    0x20: 'sla b',
    0x21: 'sla c',
    0x22: 'sla d',
    0x23: 'sla e',
    0x24: 'sla h',
    0x25: 'sla l',
    0x26: 'sla [hl]',
    0x27: 'sla a',
    0x28: 'sra b',
    0x29: 'sra c',
    0x2a: 'sra d',
    0x2b: 'sra e',
    0x2c: 'sra h',
    0x2d: 'sra l',
    0x2e: 'sra [hl]',
    0x2f: 'sra a',
    
    0x30: 'swap b',
    0x31: 'swap c',
    0x32: 'swap d',
    0x33: 'swap e',
    0x34: 'swap h',
    0x35: 'swap l',
    0x36: 'swap [hl]',
    0x37: 'swap a',
    0x38: 'srl b',
    0x39: 'srl c',
    0x3a: 'srl d',
    0x3b: 'srl e',
    0x3c: 'srl h',
    0x3d: 'srl l',
    0x3e: 'srl [hl]',
    0x3f: 'srl a',
    
    0x40: 'bit 0,b',
    0x41: 'bit 0,c',
    0x42: 'bit 0,d',
    0x43: 'bit 0,e',
    0x44: 'bit 0,h',
    0x45: 'bit 0,l',
    0x46: 'bit 0,[hl]',
    0x47: 'bit 0,a',
    0x48: 'bit 1,b',
    0x49: 'bit 1,c',
    0x4a: 'bit 1,d',
    0x4b: 'bit 1,e',
    0x4c: 'bit 1,h',
    0x4d: 'bit 1,l',
    0x4e: 'bit 1,[hl]',
    0x4f: 'bit 1,a',
    
    0x50: 'bit 2,b',
    0x51: 'bit 2,c',
    0x52: 'bit 2,d',
    0x53: 'bit 2,e',
    0x54: 'bit 2,h',
    0x55: 'bit 2,l',
    0x56: 'bit 2,[hl]',
    0x57: 'bit 2,a',
    0x58: 'bit 3,b',
    0x59: 'bit 3,c',
    0x5a: 'bit 3,d',
    0x5b: 'bit 3,e',
    0x5c: 'bit 3,h',
    0x5d: 'bit 3,l',
    0x5e: 'bit 3,[hl]',
    0x5f: 'bit 3,a',
    
    0x60: 'bit 4,b',
    0x61: 'bit 4,c',
    0x62: 'bit 4,d',
    0x63: 'bit 4,e',
    0x64: 'bit 4,h',
    0x65: 'bit 4,l',
    0x66: 'bit 4,[hl]',
    0x67: 'bit 4,a',
    0x68: 'bit 5,b',
    0x69: 'bit 5,c',
    0x6a: 'bit 5,d',
    0x6b: 'bit 5,e',
    0x6c: 'bit 5,h',
    0x6d: 'bit 5,l',
    0x6e: 'bit 5,[hl]',
    0x6f: 'bit 5,a',

    0x70: 'bit 6,b',
    0x71: 'bit 6,c',
    0x72: 'bit 6,d',
    0x73: 'bit 6,e',
    0x74: 'bit 6,h',
    0x75: 'bit 6,l',
    0x76: 'bit 6,[hl]',
    0x77: 'bit 6,a',
    0x78: 'bit 7,b',
    0x79: 'bit 7,c',
    0x7a: 'bit 7,d',
    0x7b: 'bit 7,e',
    0x7c: 'bit 7,h',
    0x7d: 'bit 7,l',
    0x7e: 'bit 7,[hl]',
    0x7f: 'bit 7,a', 

    0x80: 'res 0,b',
    0x81: 'res 0,c',
    0x82: 'res 0,d',
    0x83: 'res 0,e',
    0x84: 'res 0,h',
    0x85: 'res 0,l',
    0x86: 'res 0,[hl]',
    0x87: 'res 0,a',
    0x88: 'res 1,b',
    0x89: 'res 1,c',
    0x8a: 'res 1,d',
    0x8b: 'res 1,e',
    0x8c: 'res 1,h',
    0x8d: 'res 1,l',
    0x8e: 'res 1,[hl]',
    0x8f: 'res 1,a',
    
    0x90: 'res 2,b',
    0x91: 'res 2,c',
    0x92: 'res 2,d',
    0x93: 'res 2,e',
    0x94: 'res 2,h',
    0x95: 'res 2,l',
    0x96: 'res 2,[hl]',
    0x97: 'res 2,a',
    0x98: 'res 3,b',
    0x99: 'res 3,c',
    0x9a: 'res 3,d',
    0x9b: 'res 3,e',
    0x9c: 'res 3,h',
    0x9d: 'res 3,l',
    0x9e: 'res 3,[hl]',
    0x9f: 'res 3,a',
    
    0xa0: 'res 4,b',
    0xa1: 'res 4,c',
    0xa2: 'res 4,d',
    0xa3: 'res 4,e',
    0xa4: 'res 4,h',
    0xa5: 'res 4,l',
    0xa6: 'res 4,[hl]',
    0xa7: 'res 4,a',
    0xa8: 'res 5,b',
    0xa9: 'res 5,c',
    0xaa: 'res 5,d',
    0xab: 'res 5,e',
    0xac: 'res 5,h',
    0xad: 'res 5,l',
    0xae: 'res 5,[hl]',
    0xaf: 'res 5,a',

    0xb0: 'res 6,b',
    0xb1: 'res 6,c',
    0xb2: 'res 6,d',
    0xb3: 'res 6,e',
    0xb4: 'res 6,h',
    0xb5: 'res 6,l',
    0xb6: 'res 6,[hl]',
    0xb7: 'res 6,a',
    0xb8: 'res 7,b',
    0xb9: 'res 7,c',
    0xba: 'res 7,d',
    0xbb: 'res 7,e',
    0xbc: 'res 7,h',
    0xbd: 'res 7,l',
    0xbe: 'res 7,[hl]',
    0xbf: 'res 7,a',


    0xc0: 'set 0,b',
    0xc1: 'set 0,c',
    0xc2: 'set 0,d',
    0xc3: 'set 0,e',
    0xc4: 'set 0,h',
    0xc5: 'set 0,l',
    0xc6: 'set 0,[hl]',
    0xc7: 'set 0,a',
    0xc8: 'set 1,b',
    0xc9: 'set 1,c',
    0xca: 'set 1,d',
    0xcb: 'set 1,e',
    0xcc: 'set 1,h',
    0xcd: 'set 1,l',
    0xce: 'set 1,[hl]',
    0xcf: 'set 1,a',
    
    0xd0: 'set 2,b',
    0xd1: 'set 2,c',
    0xd2: 'set 2,d',
    0xd3: 'set 2,e',
    0xd4: 'set 2,h',
    0xd5: 'set 2,l',
    0xd6: 'set 2,[hl]',
    0xd7: 'set 2,a',
    0xd8: 'set 3,b',
    0xd9: 'set 3,c',
    0xda: 'set 3,d',
    0xdb: 'set 3,e',
    0xdc: 'set 3,h',
    0xdd: 'set 3,l',
    0xde: 'set 3,[hl]',
    0xdf: 'set 3,a',
    
    0xe0: 'set 4,b',
    0xe1: 'set 4,c',
    0xe2: 'set 4,d',
    0xe3: 'set 4,e',
    0xe4: 'set 4,h',
    0xe5: 'set 4,l',
    0xe6: 'set 4,[hl]',
    0xe7: 'set 4,a',
    0xe8: 'set 5,b',
    0xe9: 'set 5,c',
    0xea: 'set 5,d',
    0xeb: 'set 5,e',
    0xec: 'set 5,h',
    0xed: 'set 5,l',
    0xee: 'set 5,[hl]',
    0xef: 'set 5,a',

    0xf0: 'set 6,b',
    0xf1: 'set 6,c',
    0xf2: 'set 6,d',
    0xf3: 'set 6,e',
    0xf4: 'set 6,h',
    0xf5: 'set 6,l',
    0xf6: 'set 6,[hl]',
    0xf7: 'set 6,a',
    0xf8: 'set 7,b',
    0xf9: 'set 7,c',
    0xfa: 'set 7,d',
    0xfb: 'set 7,e',
    0xfc: 'set 7,h',
    0xfd: 'set 7,l',
    0xfe: 'set 7,[hl]',
    0xff: 'set 7,a'
}
