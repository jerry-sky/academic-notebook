package com.example.pingouin.model

import androidx.room.*

@Entity(tableName = "game_state")
data class GameState(
    val scoreLeft: Int,
    val scoreRight: Int,
    @PrimaryKey
    val uid: Int = 1,
)

@Dao
interface GameStateDao {
    @Query("SELECT * FROM game_state LIMIT 1")
    fun getState(): GameState?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun saveState(state: GameState)

    @Query("DELETE FROM game_state")
    fun reset()
}

@Database(entities = [GameState::class], version = 1)
abstract class GameDatabase : RoomDatabase() {
    abstract fun gameState(): GameStateDao
}
