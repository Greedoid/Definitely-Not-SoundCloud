import sqlite3
import json

def insert_song(title, artist, year, lyrics): 
	conn = sqlite3.connect('lyrics.db')
	lyrical_string = str(lyrics)
	conn.execute("INSERT INTO songs(Title, Artist, Year, Lyrics) VALUES (?, ?, ?, ?)", (title, artist, year, lyrical_string),)
	conn.commit()
	if conn:
		conn.close()

def get_lyrics_by_title(title): # Retrieves the class of a particular suggestion
	conn = sqlite3.connect('lyrics.db')
	cur = conn.cursor()
	cur.execute("SELECT Lyrics FROM songs WHERE Title = ?", [title])
	classified = cur.fetchone()
	if conn: 
		conn.close()
	return (classified)

def get_lyrics_by_year(year):
	conn = sqlite3.connect('lyrics.db')
	cur = conn.cursor()
	cur.execute("SELECT Lyrics FROM songs WHERE Year = ?", [year])
	lyric_sum = cur.fetchall()
	#cleanedup = [str(elem[0]) for elem in lyric_sum]
	if conn:
		conn.close()
	return lyric_sum 

