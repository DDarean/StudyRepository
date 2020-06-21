from flask import Flask, render_template, request, escape, session
from flask import copy_current_request_context
import vsearch

from DBcm import UseDatabase, UserException, CredentialsError, SQLError
from checker import check_logged_in
from threading import Thread

app = Flask(__name__)

app.config['dbconfig'] = {'host':'127.0.0.1',
							'user':'vsearch',
							'password':'vsearchpasswd',
							'database':'vsearchlogDB',}





@app.route('/search4',methods=['POST'])
                
def do_search() -> 'html':
	@copy_current_request_context
	def log_request(req: 'flask_request', res: str) -> None:
		with UseDatabase(app.config['dbconfig']) as cursor:	
			_SQL = """insert into log
						(phrase, letters,ip,browser_string,results)
						values
						(%s,%s,%s,%s,%s)"""
			cursor.execute(_SQL, (req.form['phrase'], req.form['letters'],req.remote_addr,req.user_agent.browser, res, ))
	
	phrase = request.form['phrase']
	letters = request.form['letters']
	title = 'Here are your results: '
	results = str(vsearch.search4letters(phrase,letters))
	try:
		t = Thread(target=log_request, args=(request,results))
		t.start()
	except Exception as err:
		print ('Error occured: ', str(err))
	return render_template('results.html',the_phrase = phrase,the_letters = letters,the_title = title,the_results = results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
	return render_template('entry.html', the_title='Welcome to search4letters on the web!')
	
@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
	try:
		with UseDatabase(app.config['dbconfig']) as cursor:	
			_SQL = """select ts, phrase, letters, ip, browser_string,results from log"""
			cursor.execute(_SQL)
			contents = cursor.fetchall()
		titles = ('TimeStamp', 'Phrase','Letters', 'Remote_addr', 'User_agent', 'Results')
		return render_template('viewlog.html',
								the_title='View Log',
								the_row_titles=titles,
								the_data=contents,)
	except CredentialsError as err:
		print('Credentials Error', str(err))
	except UserException as err:
		print('User exception', str(err))
	except SQLError as err:
		print('Query error: ', str(err))
	except Exception as err:
		print('Something went wrong:', str(err))
							
@app.route('/login')
def do_login() -> str:
	session['logged_in'] = True
	return 'You are now logged_in.'
	
app.secret_key = 'keykeykey'

@app.route('/logout')
def do_logout() -> str:
	session.pop('logged_in')
	return 'You are now logged_out.'

if __name__ == '__main__':
	app.run(debug=True)


