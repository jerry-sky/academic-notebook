import { ListOfPoint3D, Point3D } from '../types';
import { MyCanvas, Shape } from './canvas';

export class Game {

    private bulletWidth = 0.01
    private bulletHeight = 0.1
    private bullet: Shape
    private bulletGoing = false
    private bulletVelocity = 0.001

    private playerSize = 0.15
    private player: Shape

    private opponentsHit = 0
    private opponentWidth = 0.15
    private opponentHeight = 0.08
    private opponents: Shape[]

    private lastTime = performance.now()

    constructor(
        private myCanvas: MyCanvas,
        private opponentsCount = 10
    ) {
        this.setupListeners()
        this.makeNewGame()
        this.animate(performance.now())
    }

    public makeNewGame() {

        this.myCanvas.resetShapes()
        // the bullet that the players uses to annihilate the opponents
        this.bullet = {
            colour: [1, 1, 1],
            drawType: this.myCanvas.DrawTypes.TRIANGLE_FAN,
            points: new ListOfPoint3D([
                new Point3D(0, 0, 0),
                new Point3D(0, this.bulletHeight, 0),
                new Point3D(this.bulletWidth, this.bulletHeight, 0),
                new Point3D(this.bulletWidth, 0, 0)
            ])
        }
        this.myCanvas.addShape(this.bullet)
        this.bullet.points.translate(new Point3D(0, -2, 0.1))

        this.player = {
            colour: [1, 0, 1],
            drawType: this.myCanvas.DrawTypes.TRIANGLE_FAN,
            points: new ListOfPoint3D([
                new Point3D(0, 0, 0),
                new Point3D(0, this.playerSize, 0),
                new Point3D(this.playerSize, this.playerSize, 0),
                new Point3D(this.playerSize, 0, 0),
            ])
        }
        this.myCanvas.addShape(this.player)
        this.player.points.translate(new Point3D(0, -1, 0))

        // add opponents
        this.opponents = []
        for (let i = 0; i < this.opponentsCount; i++) {
            const opponent = {
                colour: [0, 1, 0],
                drawType: this.myCanvas.DrawTypes.TRIANGLE_FAN,
                points: new ListOfPoint3D([
                    new Point3D(0, 0, 0),
                    new Point3D(0, this.opponentHeight, 0),
                    new Point3D(this.opponentWidth, this.opponentHeight, 0),
                    new Point3D(this.opponentWidth, 0, 0)
                ])
            }
            this.opponents.push(opponent)
            this.myCanvas.addShape(opponent)
            opponent.points.translate(new Point3D(-1 + i * 0.2 + 0.025, 0, 0))
        }

        this.bulletGoing = false

    }

    public animate(time: number) {

        const timeDelta = time - this.lastTime
        this.lastTime = time

        if (this.bulletGoing) {
            this.bullet.points.translateY(timeDelta * this.bulletVelocity)
            if (this.bullet.points[0].y > 1) {
                this.bulletGoing = false
            }

            const bulletOrigin = this.bullet.points[1]
            // check for collisions
            for (const opponent of this.opponents) {
                const origin = opponent.points[0]
                if (
                    origin.y <= bulletOrigin.y
                    && origin.x <= bulletOrigin.x
                    && origin.x + this.opponentWidth >= bulletOrigin.x
                ) {
                    console.log('hit')
                    this.bulletGoing = false
                    opponent.points.translateY(2)
                    this.bullet.points.translateY(2)
                    this.opponentsHit++

                    if (this.opponentsHit === this.opponentsCount) {
                        alert('Level cleared')
                    }
                }
            }
        }

        window.requestAnimationFrame(this.animate.bind(this))

    }

    private setupListeners() {
        window.addEventListener('keydown', (event) => {

            switch (event.key) {
                case 'ArrowLeft':
                    this.player.points.translate(new Point3D(-0.1, 0, 0))
                    break
                case 'ArrowRight':
                    this.player.points.translate(new Point3D(0.1, 0, 0))
                    break
                case ' ': // space bar
                    // fire the bullet
                    // set the bullet’s position to that of the player’s top
                    const begin = Point3D.from(this.player.points[1])
                    begin.translate(new Point3D(
                        this.playerSize / 2 - this.bulletWidth / 2,
                        0,
                        0.1
                    ))
                    //. center it
                    this.bullet.points.reset(begin)
                    // fire it
                    this.bulletGoing = true
                    break
            }

        })
    }

}
