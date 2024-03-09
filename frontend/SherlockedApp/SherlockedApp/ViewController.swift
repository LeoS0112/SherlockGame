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
    let triggerDistance: CGFloat = 30
    var currentScene: Scene = .lobbyScene
    
    // Lobby views and environment
    
    @IBOutlet weak var lobbyView: UIView!
    @IBOutlet weak var lobbyDoorView: UIView!
    
    // Office views and environment
    
    @IBOutlet weak var officeView: UIView!
    @IBOutlet weak var watsonView: UIImageView!
    
    
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
        
        let initialLocation = CGPoint(x: self.imageViewSize.width/2, y: holderView.frame.height/2)
        sherlockView.center = initialLocation
                
        let finalLocation = CGPoint(x: holderView.frame.width/2, y: holderView.frame.height/2)
        
        print(currentScene)
        print(holderView.frame)
        print(holderView.bounds)
        
        UIView.animate(withDuration: 0.5) {
            self.sherlockView.center = finalLocation
        }
        
        let twoFingerTapGesture = UITapGestureRecognizer(target: self, action: #selector(moveCharacter(_:)))
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
            if (tapLocation.x >= holderView.bounds.width - triggerDistance) {
                // Move the imageView to the door and trigger an action
                moveSherlockToLobbyDoor()
                return
            }
        case .officeScene:
            if (tapLocation.y <= watsonView.frame.size.height + triggerDistance) {
                // move to watson
                moveSherlockToWatson()
                return
            }
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
        
        let maxMargin = imageViewSize.width / 2
        
        adjustedLocation.x = max(tapLocation.x, maxMargin)
        adjustedLocation.x = min(tapLocation.x, holderView.bounds.width - maxMargin)
        
        adjustedLocation.y = max(tapLocation.y, maxMargin)
        adjustedLocation.y = min(tapLocation.y, holderView.bounds.height - maxMargin)
        
        UIView.animate(withDuration: 0.5) {
            self.sherlockView.center = adjustedLocation
        }
    }
    
    func moveSherlockToWatson() {
        
        guard let holderView = sherlockView.superview else {
            return
        }
                
        UIView.animate(withDuration: 0.8) {
            self.sherlockView.center = CGPoint(x: self.watsonView.frame.origin.x, y: self.watsonView.frame.origin.y + self.imageViewSize.height / 2)
        } completion: {_ in
            self.triggerWatsonInteraction()
        }
    }
    
    
    func moveSherlockToLobbyDoor() {
        
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
    
    @objc func triggerWatsonInteraction() {
        print("Watson triggered!")
    }
    
}

