describe('blog app', () => {
  
  context('Register', () => {
      beforeEach(() => {
        cy.visit('/register')
      })
    
      it('.type() - type into a DOM element', () => {
        cy.get('[id=el]')
          .type('fake@email.com').should('have.value', 'fake@email.com')
          .clear()
          .type('slow.typing@email.com', { delay: 100 })
          .should('have.value', 'slow.typing@email.com')
      })
    
      it('.clear() - clears an input or textarea element', () => {
        cy.get('[id=firstname]').type('Clear this text')
          .should('have.value', 'Clear this text')
          .clear()
          .should('have.value', '')
      })
    
      it('.submit() - submit a form and register', () => {
        cy.get('form')
          .find('[id=firstname]').type('Firstname')
        cy.get('form')
          .find('[id=lastname]').type('Lastname')
        cy.get('form')
          .find('[id=el]').type('test@test.test')
        cy.get('form')
          .find('[id=ur]').type('Testuser')
        cy.get('form')
          .find('[id=pwr]').type(']DBL^<-TU,R*p>rh')
        cy.get('form')
          .find('[id=pass]').type(']DBL^<-TU,R*p>rh')
    
        cy.get('form').submit()
        cy.url().should('match', /login/)
        cy.wait(1000)
      })
  })

  context('Login', () => {
      beforeEach(() => {
        cy.visit('/login')
        cy.wait(1000)
      })
    
      it('.type() - type into a DOM element', () => {
        cy.get('[id=user]')
          .type('testuser').should('have.value', 'testuser')
          .clear()
          .type('slowtestuser', { delay: 100 })
          .should('have.value', 'slowtestuser')
      })
    
      it('.clear() - clears an input or textarea element', () => {
        cy.get('[id=user]').type('Clear this text')
          .should('have.value', 'Clear this text')
          .clear()
          .should('have.value', '')
      })
    
      it('submit a form and log in', () => {
        cy.login('yershykhin', ']DBL^<-TU,R*p>rh')
        cy.url().should(
          'be.equal',
          `${Cypress.config("baseUrl")}/`
        )
        cy.wait(1000)
      })
  })

  context('View posts', () => {
    beforeEach(() => {
      cy.visit('/')
      cy.wait(1000)
    })
  
    it('go to post', () => {
        cy.get('h3')
          .contains('Bobsleigh')
          .click()
        cy.url()
          .should(
            'be.equal',
            `${Cypress.config("baseUrl")}/post/28`
          )
        cy.wait(1000)
    })

    it('display edit buttons', () => {
      cy.get('h3')
          .contains('Bobsleigh')
          .click()
      cy.url().should(
            'be.equal',
            `${Cypress.config("baseUrl")}/post/28`
          )
      cy.wait(1000)
      cy.visit('/login')
      cy.login('yershykhin', ']DBL^<-TU,R*p>rh')
      cy.wait(1000)
      cy.visit(`${Cypress.config("baseUrl")}/post/28`)
      cy.wait(1000)
      cy.get('.btn-danger')
      cy.get('.btn-primary')
    })
  })

  context('Create post', () => {
    beforeEach(() => {
      cy.visit('/')
      cy.wait(1000)
    })
    it('create post', () => {
      cy.visit('/login')
      cy.login('yershykhin', ']DBL^<-TU,R*p>rh')
      cy.wait(1000)
      cy.visit(`${Cypress.config("baseUrl")}/post/create`)
      cy.wait(1000)
      cy.get('form')
        .find('[id=Title]')
        .type('cypress post title')
      cy.get('form')
        .find('[id=Category]')
        .select(2)
      cy.get('form')
        .find('[id=Body]')
        .type('cypress post body')
      cy.get('form').submit()
      cy.wait(1000)
      cy.url().should(
        'be.equal',
        `${Cypress.config("baseUrl")}/`
      )
      cy.get('h3')
        .contains('cypress post title')
    })
  })
  context('Update post', () => {
    beforeEach(() => {
      cy.visit('/')
      cy.wait(1000)
    })
    it('update post', () => {
      cy.visit('/login')
      cy.login('yershykhin', ']DBL^<-TU,R*p>rh')
      cy.wait(1000)
      cy.get('li>span')
        .contains('Serhii Yershykhin')
        .parent()
        .find('h3>a')
        .click()
      cy.get('.btn-primary')
        .click()
      cy.wait(1000)
      cy.get('form')
        .find('[id=Title]')
        .clear()
        .type('cypress post title update')
      cy.get('form')
        .find('[id=Category]')
        .select(1)
      cy.get('form')
        .find('[id=Body]')
        .clear()
        .type('cypress post body update')
      cy.get('form').submit()
      cy.wait(1000)
      cy.url().should(
        'be.equal',
        `${Cypress.config("baseUrl")}/`
      )
      cy.get('h3')
        .contains('cypress post title update')
    })
  })

  
})