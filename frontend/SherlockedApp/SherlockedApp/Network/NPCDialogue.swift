//
//  DialogModel.swift
//  SherlockedApp
//
//  Created by Alok Sahay on 10.03.2024.
//

import Foundation

struct NPCDialogue: Codable {
    
    let npcDialogueID: Int
    let npcID: Int
    let levelID: Int
    let npcResponse: String
    
    enum CodingKeys: String, CodingKey {
        case npcDialogueID = "npc_dialouge_ID"
        case npcID = "npc_ID"
        case levelID = "level_ID"
        case npcResponse = "npc_response"
    }
}

struct DialogueRequest: Codable {
    let npcID: Int
    let levelID: Int
    let userInput: String
    
    enum CodingKeys: String, CodingKey {
        case npcID = "npc_ID"
        case levelID = "level_ID"
        case userInput = "user_input"
    }
}
