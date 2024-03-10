//
//  NPCModel.swift
//  SherlockedApp
//
//  Created by Alok Sahay on 10.03.2024.
//

import Foundation

struct NPCModel: Codable {
    let npcId: Int
    let npcName: String
    
    enum CodingKeys: String, CodingKey {
        case npcId = "npc_ID"
        case npcName = "name"
    }
}
