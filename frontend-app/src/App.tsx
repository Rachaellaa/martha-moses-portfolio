
import { useEffect, useState } from 'react'
import './App.css'
import {
  getProfile,
  getProjects,
  getExperience,
  getSkills,
  sendContactMessage,
  type Profile,
  type Project,
  type Experience,
  type Skill,
} from './api'
declare global {
  interface Window {
    gtag?: (
      command: 'event',
      eventName: string,
      eventParams?: Record<string, string>
    ) => void
  }
}

function App() {
  const [profile, setProfile] = useState<Profile | null>(null)
  const [profileLoading, setProfileLoading] = useState(true)
  const [profileError, setProfileError] = useState(false)

  const [projects, setProjects] = useState<Project[]>([])
  const [projectsLoading, setProjectsLoading] = useState(true)
  const [projectsError, setProjectsError] = useState(false)
  const [activeFilter, setActiveFilter] = useState('All')
  
  const [experiences, setExperiences] = useState<Experience[]>([])
  const [experienceLoading, setExperienceLoading] = useState(true)
  const [experienceError, setExperienceError] = useState(false)  

  const [skills, setSkills] = useState<Skill[]>([])
  const [skillsLoading, setSkillsLoading] = useState(true)
  const [skillsError, setSkillsError] = useState(false)

const [contactForm, setContactForm] = useState({
  name: '',
  email: '',
  subject: '',
  message: '',
})

const [contactLoading, setContactLoading] = useState(false)
const [contactStatus, setContactStatus] = useState('')
const [contactError, setContactError] = useState('')

  useEffect(() => {
    getProfile()
      .then((data) => {
        setProfile(data)
        setProfileError(false)
      })
      .catch((error) => {
        console.error('Could not load profile:', error)
        setProfileError(true)
      })
      .finally(() => {
        setProfileLoading(false)
      })

    getProjects()
      .then((data) => {
        setProjects(data)
        setProjectsError(false)
      })
      .catch((error) => {
        console.error('Could not load projects:', error)
        setProjectsError(true)
      })
      .finally(() => {
        setProjectsLoading(false)
      })

    getExperience()
      .then((data) => {
        setExperiences(data)
        setExperienceError(false)
      })
      .catch((error) => {
        console.error('Could not load experience:', error)
        setExperienceError(true)
      })
      .finally(() => {
        setExperienceLoading(false)
      })

    getSkills()
  .then((data) => {
    console.log('Skills received from API:', data)
    setSkills(data)
  })
  .catch((error) => {
    console.error('Skills API error:', error)
    setSkillsError(true)
  })
  .finally(() => setSkillsLoading(false))
  }, [])


  const name = profile?.full_name || 'Martha Rachael Moses'
  const title =
    profile?.professional_title ||
    'Data Engineer | Analytics Engineer | Data Analyst'
  const bio =
    profile?.short_bio ||
    'I build reliable data pipelines, scalable data platforms, and intelligent data solutions that transform complex information into meaningful business outcomes.'
  const location = profile?.location || 'Lagos, Nigeria'
  const github =
    profile?.github_url || 'https://github.com/Rachaellaa'
  const linkedin =
    profile?.linkedin_url ||
    'https://www.linkedin.com/in/martha-rachael-moses-7106253a4/'

const handleContactSubmit = async (
  event: React.FormEvent<HTMLFormElement>
) => {
  event.preventDefault()

  setContactLoading(true)
  setContactStatus('')
  setContactError('')

  try {
        const response = await sendContactMessage(contactForm)

    // Track successful contact form submissions in Google Analytics
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'contact_form_submit', {
        event_category: 'engagement',
        event_label: 'Portfolio Contact Form',
      })
    }

    setContactStatus(
      response.message || 'Your message has been sent successfully!'
    )

    setContactForm({
      name: '',
      email: '',
      subject: '',
      message: '',
    })
  } catch (error) {
    setContactError(
      error instanceof Error
        ? error.message
        : 'Something went wrong. Please try again.'
    )
  } finally {
    setContactLoading(false)
  }
}  

const filters = [
    'All',
    'Data Engineering',
    'Data Analytics & Business Intelligence',
  ]

  const filteredProjects =
    activeFilter === 'All'
      ? projects
      : projects.filter((project) => project.category === activeFilter)

  return (
    <main>
      <nav className="navbar">
        <a href="#home" className="brand">
          MRM<span>.</span>
        </a>

        <div className="nav-links">
          <a href="#about">About</a>
          <a href="#skills">Expertise</a>
          <a href="#projects">Projects</a>
          <a href="#experience">Experience</a>
          <a href="#contact">Contact</a>
        </div>

        <a href="#contact" className="nav-button">
          Let's Connect <span>↗</span>
        </a>
      </nav>

      <section className="hero-section" id="home">
        <div className="hero-content">
          <div className="availability">
            <span className="status-dot"></span>
            {profileLoading ? 'LOADING PROFILE...' : title.toUpperCase()}
          </div>

          <p className="hero-greeting">
            Hello, I'm {name}.
          </p>

          <h1>
            Engineering Data.
            <br />
            <span>Creating Impact.</span>
          </h1>

          <p className="hero-description">
            {bio}
          </p>

          <div className="hero-actions">
            <a href="#projects" className="primary-button">
              Explore My Work <span>↗</span>
            </a>

            <a href="#contact" className="secondary-button">
              Get In Touch
            </a>
          </div>

          <div className="hero-location">
            <span>⌖</span> {location}
            <span className="location-divider">/</span>
            Open to opportunities
          </div>

          {profileError && (
            <p className="section-label">
              Showing saved profile details. Live API connection unavailable.
            </p>
          )}
        </div>

        <div className="hero-visual">
          <div className="visual-glow"></div>

          <div className="data-card main-data-card">
            <div className="card-top">
              <span className="card-indicator"></span>
              DATA ENGINEERING
              <span className="card-menu">•••</span>
            </div>

            <div className="data-illustration">
              <div className="data-node source-node">
                <span>01</span>
                <strong>Sources</strong>
                <small>Raw Data</small>
              </div>

              <div className="data-line"></div>

              <div className="data-node pipeline-node">
                <span>02</span>
                <strong>Pipeline</strong>
                <small>Transform</small>
              </div>

              <div className="data-line"></div>

              <div className="data-node warehouse-node">
                <span>03</span>
                <strong>Warehouse</strong>
                <small>Insights</small>
              </div>
            </div>

            <div className="card-footer">
              <span>BUILDING DATA SYSTEMS</span>
              <span className="footer-status">● ACTIVE</span>
            </div>
          </div>

          <div className="floating-tag tag-python">Python</div>
          <div className="floating-tag tag-sql">SQL</div>
          <div className="floating-tag tag-cloud">CLOUD</div>
        </div>

        <div className="hero-bottom">
          <span>DATA ENGINEERING</span>
          <span>ANALYTICS ENGINEERING</span>
          <span>BUSINESS INTELLIGENCE</span>
          <span>DATA ANALYTICS</span>
        </div>
      </section>

      <section className="technology-section" id="skills">
  <div className="section-label">TECHNOLOGIES & TOOLS</div>

  {skillsLoading ? (
    <p className="projects-message">Loading skills...</p>
  ) : skillsError ? (
    <p className="projects-message">Unable to load skills at the moment.</p>
  ) : (
    <div className="skills-categories">
      {skills.map((group) => (
        <div className="skill-category" key={group.category}>
          <h3>{group.category}</h3>

          <div className="technology-list">
            {group.skills.map((skill) => (
              <span key={skill} className="technology-item">
                {skill}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  )}
</section>

      <section className="about-section" id="about">
        <div className="section-heading">
          <span className="section-label">01 / ABOUT ME</span>
          <h2>
            Building the infrastructure
            <br />
            <span>behind better decisions.</span>
          </h2>
        </div>

        <div className="about-content">
          <p>{bio}</p>

          <p>
            From data integration and transformation to warehousing,
            cloud platforms, and reporting, I bring together engineering
            and analytical thinking to solve practical business problems.
          </p>

          <a href="#experience" className="text-link">
            Discover my experience <span>↗</span>
          </a>
        </div>
      </section>

      <section className="projects-section" id="projects">
        <div className="section-heading">
          <span className="section-label">02 / SELECTED WORK</span>
          <h2>
            Projects that turn
            <br />
            <span>data into direction.</span>
          </h2>
        </div>

        <div className="project-filters">
          {filters.map((filter) => (
            <button
              key={filter}
              type="button"
              className={`project-filter ${
                activeFilter === filter ? 'active' : ''
              }`}
              onClick={() => setActiveFilter(filter)}
            >
              {filter === 'Data Analytics & Business Intelligence'
                ? 'Analytics & BI'
                : filter}
            </button>
          ))}
        </div>

        {projectsLoading && (
          <div className="projects-message">
            Loading projects from portfolio database...
          </div>
        )}

        {projectsError && (
          <div className="projects-message">
            Unable to load projects. Please check the backend connection.
          </div>
        )}

        {!projectsLoading && !projectsError && projects.length === 0 && (
          <div className="projects-message">
            No projects have been added yet.
          </div>
        )}

        {!projectsLoading && !projectsError && projects.length > 0 && (
          <div className="projects-grid">
            {filteredProjects.map((project, index) => (
              <article
                className="project-card"
                key={project.id ?? project.title}
              >
                <div className="project-card-top">
                  <span className="project-number">
                    PROJECT {String(index + 1).padStart(2, '0')}
                  </span>

                  {project.featured && (
                    <span className="project-featured">FEATURED</span>
                  )}
                </div>

                <span className="project-category">
                  {project.category}
                </span>

                <h3>{project.title}</h3>

                <p className="project-industry">
                  {project.industry}
                </p>

                <p className="project-description">
                  {project.description}
                </p>

                <div className="project-detail">
                  <h4>THE CHALLENGE</h4>
                  <p>{project.problem_statement}</p>
                </div>

                <div className="project-detail">
                  <h4>THE SOLUTION</h4>
                  <p>{project.solution}</p>
                </div>

                <div className="project-technologies">
                  <h4>TECHNOLOGIES</h4>
                  <div className="project-tags">
                    {project.technologies.map((technology) => (
                      <span key={technology}>{technology}</span>
                    ))}
                  </div>
                </div>

                <div className="project-features">
                  <h4>KEY FEATURES</h4>
                  <ul>
                    {project.key_features.map((feature) => (
                      <li key={feature}>{feature}</li>
                    ))}
                  </ul>
                </div>

                {(project.github_url || project.live_url) && (
                  <div className="project-links">
                    {project.github_url && (
                      <a
                        href={project.github_url}
                        target="_blank"
                        rel="noreferrer"
                      >
                        GitHub Repository ↗
                      </a>
                    )}

                    {project.live_url && (
                      <a
                        href={project.live_url}
                        target="_blank"
                        rel="noreferrer"
                      >
                        Live Project ↗
                      </a>
                    )}
                  </div>
                )}
              </article>
            ))}
          </div>
        )}
      </section>

      
<section className="experience-section" id="experience">
  <div className="section-heading">
    <span className="section-label">03 / EXPERIENCE</span>
    <h2>
      Experience grounded
      <br />
      <span>in real-world data.</span>
    </h2>
  </div>

  {experienceLoading && (
    <div className="experience-placeholder">
      Loading professional experience...
    </div>
  )}

  {experienceError && (
    <div className="experience-placeholder">
      Unable to load professional experience. Please check the backend connection.
    </div>
  )}

  {!experienceLoading && !experienceError && experiences.length === 0 && (
    <div className="experience-placeholder">
      No professional experience records available.
    </div>
  )}

  {!experienceLoading && !experienceError && experiences.length > 0 && (
    <div className="experience-timeline">
      {experiences.map((experience, index) => (
        <article
          className="experience-card"
          key={`${experience.company}-${experience.start_date}`}
        >
          <div className="experience-card-side">
            <span className="experience-index">
              0{index + 1}
            </span>

            <span className="experience-period">
              {new Date(`${experience.start_date}-01T00:00:00`).toLocaleDateString(
                'en-US',
                { month: 'short', year: 'numeric' }
              )}
              {' — '}
              {experience.is_current
                ? 'Present'
                : new Date(`${experience.end_date}-01T00:00:00`).toLocaleDateString(
                    'en-US',
                    { month: 'short', year: 'numeric' }
                  )}
            </span>
          </div>

          <div className="experience-card-content">
            <span className="experience-employment">
              {experience.employment_type}
            </span>

            <h3>{experience.job_title}</h3>

            <div className="experience-company">
              {experience.company}
            </div>

            <div className="experience-location">
              {experience.location}
            </div>

            <div className="experience-responsibilities">
              <h4>RESPONSIBILITIES & ACHIEVEMENTS</h4>

              <ul>
                {experience.responsibilities.map((responsibility) => (
                  <li key={responsibility}>{responsibility}</li>
                ))}
              </ul>
            </div>

            <div className="experience-technologies">
              {experience.technologies.map((technology) => (
                <span key={technology}>{technology}</span>
              ))}
            </div>
          </div>
        </article>
      ))}
    </div>
  )}
</section>


      <section className="contact-section" id="contact">
  <span className="section-label">04 / GET IN TOUCH</span>

  <h2>
    Let's build something
    <br />
    <span>meaningful with data.</span>
  </h2>

  <p>
    Have an opportunity, a project, or an idea? I'd love to hear from you.
  </p>

  <form className="contact-form" onSubmit={handleContactSubmit}>
    <div className="contact-form-row">
      <div className="contact-field">
        <label htmlFor="contact-name">Your Name</label>
        <input
          id="contact-name"
          type="text"
          placeholder="Enter your name"
          minLength={2}
          maxLength={100}
          required
          value={contactForm.name}
          onChange={(event) =>
            setContactForm({
              ...contactForm,
              name: event.target.value,
            })
          }
        />
      </div>

      <div className="contact-field">
        <label htmlFor="contact-email">Email Address</label>
        <input
          id="contact-email"
          type="email"
          placeholder="Enter your email"
          required
          value={contactForm.email}
          onChange={(event) =>
            setContactForm({
              ...contactForm,
              email: event.target.value,
            })
          }
        />
      </div>
    </div>

    <div className="contact-field">
      <label htmlFor="contact-subject">Subject</label>
      <input
        id="contact-subject"
        type="text"
        placeholder="What would you like to discuss?"
        minLength={3}
        maxLength={150}
        required
        value={contactForm.subject}
        onChange={(event) =>
          setContactForm({
            ...contactForm,
            subject: event.target.value,
          })
        }
      />
    </div>

    <div className="contact-field">
      <label htmlFor="contact-message">Your Message</label>
      <textarea
        id="contact-message"
        placeholder="Write your message here..."
        minLength={10}
        maxLength={3000}
        rows={6}
        required
        value={contactForm.message}
        onChange={(event) =>
          setContactForm({
            ...contactForm,
            message: event.target.value,
          })
        }
      />
    </div>

    <button
      type="submit"
      className="primary-button contact-submit"
      disabled={contactLoading}
    >
      {contactLoading ? 'Sending Message...' : 'Send Message'}
      <span>↗</span>
    </button>

    {contactStatus && (
      <p className="contact-success">{contactStatus}</p>
    )}

    {contactError && (
      <p className="contact-error">{contactError}</p>
    )}
  </form>
</section>

      <footer className="footer">
        <a href="#home" className="brand">
          MRM<span>.</span>
        </a>

        <p>© 2026 {name}. All rights reserved.</p>

        <div className="footer-links">
          <a href={github} target="_blank" rel="noreferrer">
            GitHub
          </a>

          <a href={linkedin} target="_blank" rel="noreferrer">
            LinkedIn
          </a>
        </div>
      </footer>
    </main>
  )
}

export default App
