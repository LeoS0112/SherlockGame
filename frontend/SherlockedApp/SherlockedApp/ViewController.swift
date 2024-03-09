//
//  ViewController.swift
//  SherlockedApp
//
//  Created by Alok Sahay on 09.03.2024.
//

import UIKit

class ViewController: UIViewController {
    
    let sherlockView = UIImageView()
    @IBOutlet weak var lobbyView: UIView!
    @IBOutlet weak var officeView: UIView!
    @IBOutlet weak var gameMapView: UIView!
    
    let imageViewSize = CGSize(width: 80, height: 80) // Define the size as a property for easier adjustments
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        createSherlockNpc()
        moveToLobby()
    }
    
    func createSherlockNpc() {
        sherlockView.frame = CGRect(x: 0, y: 0, width: imageViewSize.width, height: imageViewSize.height)
        sherlockView.image = UIImage(named: "Sherlock_default")
        sherlockView.backgroundColor = .clear
    }
    
    func moveToLobby() {
        resetNPCInRoom(room: lobbyView)
    }
    
    func moveToOffice() {
    }
    
    func moveToGame() {
    }
    
    func resetNPCInRoom(room: UIView) {
        
        let holderView = room
        holderView.addSubview(sherlockView)
        
        sherlockView.frame = CGRect(origin: CGPoint(x: (holderView.bounds.width - imageViewSize.width) / 2, y: (holderView.bounds.height - imageViewSize.height) / 2), size: imageViewSize)
        
        let twoFingerTapGesture = UITapGestureRecognizer(target: self, action: #selector(moveCharacter(_:)))
        //        twoFingerTapGesture.numberOfTouchesRequired = 2 // Set to require two fingers for the tap
        holderView.addGestureRecognizer(twoFingerTapGesture)
    }
    
    @objc func moveCharacter(_ gesture: UITapGestureRecognizer) {
        
        guard let holderView = sherlockView.superview else {
            return
        }
        
        var tapLocation = gesture.location(in: holderView)
        
        tapLocation.x = max(tapLocation.x, imageViewSize.width / 2)
        tapLocation.x = min(tapLocation.x, holderView.bounds.width - imageViewSize.width / 2)
        
        tapLocation.y = max(tapLocation.y, imageViewSize.height / 2)
        tapLocation.y = min(tapLocation.y, holderView.bounds.height - imageViewSize.height / 2)
        
        UIView.animate(withDuration: 0.5) {
            self.sherlockView.center = tapLocation
        }
    }
    
}

