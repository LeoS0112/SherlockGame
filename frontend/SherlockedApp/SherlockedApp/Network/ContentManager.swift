//
//  ContentManager.swift
//  SherlockedApp
//
//  Created by Alok Sahay on 09.03.2024.
//

import Foundation
import UIKit

class ContentManager {
    
    static let lobbyCarpetAssetUrl = URL(string: "https://sherlock-game.s3.eu-west-2.amazonaws.com/carpets/0")
    static let officeCarpetAssetUrl = URL(string: "https://sherlock-game.s3.eu-west-2.amazonaws.com/carpets/1")
    static let gameCarpetAssetUrl = URL(string: "https://sherlock-game.s3.eu-west-2.amazonaws.com/carpets/2")
    static let userImageAssetUrl = URL(string: "https://sherlock-game.s3.eu-west-2.amazonaws.com/carpets")
    static let getDialogsUrl = URL(string: "https://divine-pond-3b355c38.zvgz4d.on-acorn.io/npc-dialouge/")
    static let sendDialogsUrl = URL(string: "https://divine-pond-3b355c38.zvgz4d.on-acorn.io/user-dialouge/")
    static let getNPCsUrl = URL(string: "https://divine-pond-3b355c38.zvgz4d.on-acorn.io/npcs/")
    
    static func uploadUserAsset(image: UIImage, completion: @escaping (UIImage?, Error?) -> Void) {
        
        
        
        
    }
    
    
    static func fetchAsset(assetURL: URL?, completion: @escaping (UIImage?, Error?) -> Void) {
        guard let url = assetURL else {
            completion(nil, NSError(domain: "InvalidURL", code: 404, userInfo: nil))
            return
        }
        
        URLSession.shared.dataTask(with: url) { data, response, error in
            if let error = error {
                DispatchQueue.main.async {
                    completion(nil, error)
                }
                return
            }
            
            guard let data = data, let image = UIImage(data: data) else {
                DispatchQueue.main.async {
                    completion(nil, NSError(domain: "DataError", code: 404, userInfo: nil))
                }
                return
            }
            
            DispatchQueue.main.async {
                completion(image, nil)
            }
        }.resume()
    }
    
    static func getConversations(url: URL?, completion: @escaping ([NPCDialogue]?, Error?) -> Void) {
        guard let url = url else { return }
        
        URLSession.shared.dataTask(with: url) { (data, response, error) in
            if let error = error {
                print("Error with fetching dialogues: \(error.localizedDescription)")
                return
            }
            
            guard let data = data else {
                print("No data received")
                return
            }
            
            do {
                let decoder = JSONDecoder()
                decoder.keyDecodingStrategy = .useDefaultKeys // If you prefer automatic conversion
                let dialogues = try decoder.decode([NPCDialogue].self, from: data)
                
                DispatchQueue.main.async {
                    completion(dialogues,nil)
                }
                
            } catch {
                print("Error decoding JSON: \(error.localizedDescription)")
            }
        }.resume()
    }
    
    static func getNPCs(url: URL?, completion: @escaping ([NPCModel]?, Error?) -> Void) {
        guard let url = url else { return }
        
        URLSession.shared.dataTask(with: url) { (data, response, error) in
            if let error = error {
                print("Error with fetching dialogues: \(error.localizedDescription)")
                return
            }
            
            guard let data = data else {
                print("No data received")
                return
            }
            
            do {
                let decoder = JSONDecoder()
                decoder.keyDecodingStrategy = .useDefaultKeys // If you prefer automatic conversion
                let npcs = try decoder.decode([NPCModel].self, from: data)
                
                DispatchQueue.main.async {
                    completion(npcs,nil)
                }
                
            } catch {
                print("Error decoding JSON: \(error.localizedDescription)")
            }
        }.resume()
    }
    
    static func sendConversation(url: URL?, npcId: Int, message: String, completion: @escaping (Bool, Error?) -> Void) {
        
        guard let url = url else { return }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let dialog = DialogueRequest(npcID: npcId, levelID: 1, userInput: message)
        
        guard let jsonData = try? JSONEncoder().encode(dialog) else {
            print("Error encoding request data")
            return
        }
        request.httpBody = jsonData
        
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("Error: \(error.localizedDescription)")
                completion(false, error)
                return
            }
            
            guard let httpResponse = response as? HTTPURLResponse, (200...299).contains(httpResponse.statusCode) else {
                print("Error with the response, unexpected status code: \(String(describing: response))")
                completion(false, error)
                return
            }
            
            if let data = data, let dataString = String(data: data, encoding: .utf8) {
                print("Response data string:\n \(dataString)")
                completion(true, nil)
            }
        }

        task.resume()
    }
    
}
