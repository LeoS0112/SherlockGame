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

    
}
