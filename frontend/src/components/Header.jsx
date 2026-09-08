// frontend/src/components/Header.jsx
function Header() {
  return (
    <header className="flex items-center justify-between px-8 py-4 bg-paper border-b border-paper-soft">
      <div className="flex items-center gap-2">
        <span className="text-2xl">📖</span>
        <span className="font-display text-2xl font-semibold text-primary">Kitepche</span>
      </div>

      <nav className="flex items-center gap-6 font-body">
        <a href="#" className="text-ink hover:text-primary">Home</a>
        <a href="#" className="text-ink hover:text-primary">Library</a>
        <a href="#" className="text-ink hover:text-primary">Analyze</a>
        <button className="bg-accent hover:bg-accent-dark text-white font-medium px-4 py-2 rounded-full">
          Login
        </button>
      </nav>
    </header>
  )
}

export default Header