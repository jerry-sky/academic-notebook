import { ListOfPoint3D, Point3D } from '../types'
import { MyCanvas, Shape, TextureSquare } from './canvas'

(async () => {

    const imageLoader = (imageSrc: string) => new Promise<HTMLImageElement>((resolve) => {
        const img = new Image()
        img.addEventListener('load', () => resolve(img))
        img.src = imageSrc
    })

    const canvasElement: HTMLCanvasElement = document.querySelector('canvas')

    // load the player’s avatar
    const playerTexture = await imageLoader(
        (document.querySelector('img#avatar') as HTMLImageElement).src
    )
    // load the background image
    const backgroundTexture = await imageLoader(
        (document.querySelector('img#background') as HTMLImageElement).src
    )

    const myCanvas = new MyCanvas(canvasElement)

    myCanvas.startAnimationLoop()

    // prepare decorations
    // add a background
    myCanvas.addTextureSquare({
        origin: new Point3D(-1, -1, 0.9),
        size: 2,
        texture: backgroundTexture
    })
    // add a frame
    myCanvas.addShape({
        colour: [0.5, 0.5, 0.5],
        drawType: myCanvas.DrawTypes.LINE_LOOP,
        points: new ListOfPoint3D([
            new Point3D(-1, -1, -0.9),
            new Point3D(-1, 1, -0.9),
            new Point3D(1, 1, -0.9),
            new Point3D(1, -1, -0.9),
        ])
    })

    // add a mother ship
    myCanvas.addShape({
        colour: [1, 0, 0],
        drawType: myCanvas.DrawTypes.TRIANGLE_FAN,
        points: new ListOfPoint3D([
            new Point3D(-1, 0.7, -0.4),
            new Point3D(1, 0.7, -0.4),
            new Point3D(0.5, 0.4, -0.4),
            new Point3D(-0.5, 0.4, -0.4),
        ])
    })

    // add another piece of decoration
    const decorSize = 0.9
    myCanvas.addShape({
        colour: [0.4, 0, 0.8],
        drawType: myCanvas.DrawTypes.LINE_LOOP,
        points: new ListOfPoint3D([
            new Point3D(decorSize, -decorSize, -0.6),
            new Point3D(decorSize, decorSize, -0.6),
            new Point3D(-decorSize, decorSize, -0.6),
            new Point3D(-decorSize, -decorSize, -0.6),
        ])
    })

    // the bullet that the players uses to annihilate the opponents
    const bulletWidth = 0.01
    const bulletHeight = 0.1
    const bullet: Shape = {
        colour: [1, 1, 1],
        drawType: myCanvas.DrawTypes.TRIANGLE_FAN,
        points: new ListOfPoint3D([
            new Point3D(0, 0, 0),
            new Point3D(0, bulletHeight, 0),
            new Point3D(bulletWidth, bulletHeight, 0),
            new Point3D(bulletWidth, 0, 0)
        ])
    }
    myCanvas.addShape(bullet)
    bullet.points.translate(new Point3D(0, -2, 0.1))

    const playerSize = 0.15
    const player: TextureSquare = {
        origin: new Point3D(0, 0, -0.5),
        size: playerSize,
        texture: playerTexture
    }
    myCanvas.addTextureSquare(player)
    player.origin.translate(new Point3D(0, -1, 0))

    const opponentsInARow = 8
    const opponentsCount = opponentsInARow * 2
    const opponentWidth = 1 / opponentsInARow
    const opponentHeight = 0.08
    // add opponents
    const opponents: Shape[] = []
    for (let i = 0; i < opponentsCount; i++) {
        const opponent = {
            colour: [0, 1, 0],
            drawType: myCanvas.DrawTypes.TRIANGLE_FAN,
            points: new ListOfPoint3D([
                new Point3D(0, 0, 0),
                new Point3D(0, opponentHeight, 0),
                new Point3D(opponentWidth, opponentHeight, 0),
                new Point3D(opponentWidth, 0, 0)
            ])
        }
        opponents.push(opponent)
        myCanvas.addShape(opponent)
        const row = Math.floor(i / opponentsInARow)
        opponent.points.translate(new Point3D(
            -1 + (i - row * opponentsInARow) * opponentWidth * 2 + opponentWidth / 2,
            row * opponentHeight * 1.2,
            0
        ))
    }

    let bulletGoing = false
    const bulletVelocity = 0.001

    let opponentsHit = 0

    let lastTime = performance.now()
    animate(performance.now())
    function animate(time: number) {

        const timeDelta = time - lastTime
        lastTime = time

        if (bulletGoing) {
            bullet.points.translateY(timeDelta * bulletVelocity)
            if (bullet.points[0].y > 1) {
                bulletGoing = false
            }

            const bulletOrigin = bullet.points[1]
            // check for collisions
            for (const opponent of opponents) {
                const origin = opponent.points[0]
                if (
                    origin.y <= bulletOrigin.y
                    && origin.x <= bulletOrigin.x
                    && origin.x + opponentWidth >= bulletOrigin.x
                ) {
                    bulletGoing = false
                    opponent.points.translateY(2)
                    bullet.points.translateY(2)
                    opponentsHit++

                    if (opponentsHit === opponentsCount) {
                        alert('Level cleared. Reload the page to play again.')
                    }
                    break
                }
            }
        }

        window.requestAnimationFrame(animate)

    }

    window.addEventListener('keydown', (event) => {

        switch (event.key) {
            case 'ArrowLeft':
                player.origin.translate(new Point3D(-0.1, 0, 0))
                break
            case 'ArrowRight':
                player.origin.translate(new Point3D(0.1, 0, 0))
                break
            case ' ': // space bar
                // fire the bullet
                // set the bullet’s position to that of the player’s top
                const begin = Point3D.from(player.origin)
                begin.translate(new Point3D(
                    playerSize / 2 - bulletWidth / 2,
                    0,
                    0.1
                ))
                //. center it
                bullet.points.reset(begin)
                // fire it
                bulletGoing = true
                break
        }

    })

})()
