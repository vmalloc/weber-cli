def test_add_blueprint(init_dir, cli):
    cli.run(['-w', init_dir, 'generate', 'blueprint', 'index', '--path=/'])
