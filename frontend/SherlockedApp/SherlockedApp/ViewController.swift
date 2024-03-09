//
//  ViewController.swift
//  SherlockedApp
//
//  Created by Alok Sahay on 09.03.2024.
//

import UIKit

class ViewController: UIViewController {
    
    enum Scene {
        case lobbyScene
        case officeScene
        case gameScene
    }
    
    
    let sherlockView = UIImageView()
    
    // Lobby views and environment
    
    @IBOutlet weak var lobbyView: UIView!
    @IBOutlet weak var lobbyDoorView: UIView!
    let doorTriggerDistance: CGFloat = 30
    var currentScene: Scene = .lobbyScene
    
    // Office views and environment
    
    @IBOutlet weak var officeView: UIView!
    
    // game views and environment
    
    @IBOutlet weak var gameMapView: UIView!
    
    // Sherlock NPC details
    let imageViewSize = CGSize(width: 80, height: 80) // Define the size as a property for easier adjustments
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        createSherlockNpc()
        startGame()
    }
    
    func createSherlockNpc() {
        sherlockView.frame = CGRect(x: 0, y: 0, width: imageViewSize.width, height: imageViewSize.height)
        sherlockView.image = UIImage(named: "Sherlock_default")
        sherlockView.backgroundColor = .clear
    }
    
    func startGame() {
        moveToScene(sceneLocation: .lobbyScene)
    }
    
    func moveToScene(sceneLocation: Scene) {
        
        if sceneLocation != currentScene {
            
            guard let holderView = sherlockView.superview else {
                return
            }
            holderView.gestureRecognizers?.forEach({ gesture in
                holderView.removeGestureRecognizer(gesture)
            })
            sherlockView.removeFromSuperview()
        }
        
        switch sceneLocation {
        case .lobbyScene :
            resetNPCInRoom(room: lobbyView)
            break
        case .officeScene:
            resetNPCInRoom(room: officeView)
            break
        case .gameScene:
            resetNPCInRoom(room: gameMapView)
            break
        }
        
        currentScene = sceneLocation
    }
    
    func resetNPCInRoom(room: UIView) {
        
        let holderView = room
        holderView.addSubview(sherlockView)
        
        UIView.animate(withDuration: 0.5) {
            self.sherlockView.frame = CGRect(origin: CGPoint(x: (holderView.bounds.width - self.imageViewSize.width) / 2, y: (holderView.bounds.height - self.imageViewSize.height) / 2), size: self.imageViewSize)
        }
        
        let twoFingerTapGesture = UITapGestureRecognizer(target: self, action: #selector(moveCharacter(_:)))
        //        twoFingerTapGesture.numberOfTouchesRequired = 2 // Set to require two fingers for the tap
        holderView.addGestureRecognizer(twoFingerTapGesture)
    }
    
    @objc func moveCharacter(_ gesture: UITapGestureRecognizer) {
        
        guard let holderView = sherlockView.superview else {
            return
        }
        
        let tapLocation = gesture.location(in: holderView)
        
        // Check if theres a door in the room
        
        switch currentScene {
            
        case .lobbyScene:
            if (tapLocation.x >= holderView.bounds.width - doorTriggerDistance) {
                // Move the imageView to the door and trigger an action
                moveImageViewToDoor()
                return
            }
        case .officeScene:
            break
        case .gameScene:
            break
        }
        moveImageViewWithinBounds(tapLocation: tapLocation)
    }
    
    func moveImageViewWithinBounds(tapLocation: CGPoint) {
        
        guard let holderView = sherlockView.superview else {
            return
        }
        
        var adjustedLocation = tapLocation
        
        adjustedLocation.x = max(tapLocation.x, imageViewSize.width / 2)
        adjustedLocation.x = min(tapLocation.x, holderView.bounds.width - imageViewSize.width / 2)
        
        adjustedLocation.y = max(tapLocation.y, imageViewSize.height / 2)
        adjustedLocation.y = min(tapLocation.y, holderView.bounds.height - imageViewSize.height / 2)
        
        UIView.animate(withDuration: 0.5) {
            self.sherlockView.center = adjustedLocation
        }
    }
    
    func moveImageViewToDoor() {
        
        guard let holderView = sherlockView.superview else {
            return
        }
        
        UIView.animate(withDuration: 0.8) {
            self.sherlockView.center = CGPoint(x: holderView.bounds.width - self.imageViewSize.width / 2, y: self.sherlockView.center.y)
        } completion: {_ in 
            self.triggerLobbyDoorAction()
        }
    }
    
    @objc func triggerLobbyDoorAction() {
        print("Lobby Door triggered!")
        moveToScene(sceneLocation: .officeScene)
    }
    
    
}

